from django.db import IntegrityError
from django.utils import timezone
from django.http import JsonResponse
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
import json
from django.core.exceptions import ValidationError
from django.views.decorators.csrf import csrf_exempt
import logging

from .models import Question, SolvedQuestion, ExamLog

def root_view(request):
    # Redirect authenticated users to the main page
    return redirect('question:index')

def index(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('question:main')
        else:
            # Render the login page with an error message
            return render(request, 'question/index.html', {'error': 'Invalid credentials'})
    else:
        # Render the login page
        return render(request, 'question/index.html')

@login_required
def main(request):
    # Render the main page with the username in the context
    context = {
        'username': request.user.username
    }
    return render(request, 'question/main.html', context)

def logout_view(request):
    # Log the user out and redirect to the index page
    logout(request)
    return redirect('question:index')

def signup(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        password_confirm = request.POST['password_confirm']

        # Input validation
        if not username or not password or not password_confirm:
            return render(request, 'question/signup.html', {'error': 'All fields are required'})

        if password != password_confirm:
            return render(request, 'question/signup.html', {'error': 'Passwords do not match'})

        # Handle exceptions during user creation
        try:
            user = User.objects.create_user(username=username, password=password)
            user.full_clean()  # Additional validation
            user.save()
            login(request, user)
            return redirect('question:index')
        except ValidationError as e:
            return render(request, 'question/signup.html', {'error': e.messages})
        except Exception:
            return render(request, 'question/signup.html', {'error': 'The user is already registered'})
    else:
        # Render the signup page
        return render(request, 'question/signup.html')

logger = logging.getLogger(__name__)

@login_required
@csrf_exempt
def quiz(request, chapter_num):
    current_user = request.user
    questions = Question.objects.filter(chapter=chapter_num)
    total_questions = questions.count()
    total_1 = total_questions - 1
    current_index = int(request.GET.get('q', 0))
    current_index = max(0, min(current_index, total_questions - 1))
    current_question = questions[current_index] if total_questions > 0 else None

    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            submitted_answers = data.get('answers')

            if not current_user.is_authenticated:
                logger.warning("User not authenticated")
                return JsonResponse({'success': False, 'message': 'User not authenticated'}, status=401)

            total_correctness = 0
            for i, question in enumerate(questions):
                correctness = False
                if question.answer.lower() == submitted_answers[i].lower():
                    correctness = True
                    total_correctness += 1
                solved_question, created = SolvedQuestion.objects.get_or_create(
                    user=current_user,
                    solved_questions=question,
                    defaults={'was_right': correctness, 'submitted_answer': submitted_answers[i]}
                )
                if not created:
                    # If the solved question already exists, update it
                    solved_question.was_right = correctness
                    solved_question.submitted_answer = submitted_answers[i]
                    solved_question.save()
            exam_log = ExamLog(
                user=current_user,
                chapter=chapter_num,
                exam_dateTime=timezone.now(),
                total_solved_questions=total_questions,
                total_correct_questions=total_correctness
            )
            exam_log.save()

            request.session['correct_answers'] = total_correctness
            request.session['incorrect_answers'] = total_questions - total_correctness
            request.session['total_questions'] = total_questions
            request.session['chapter_num'] = chapter_num

            return JsonResponse({'success': True})
        except IntegrityError as e:
            logger.error("IntegrityError in quiz view: %s", str(e))
            return JsonResponse({'success': False, 'message': 'Integrity error occurred: ' + str(e)}, status=500)
        except Exception as e:
            logger.error("Error in quiz view: %s", str(e), exc_info=True)
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    # Render the quiz template with the context
    context = {
        'chapter_num': chapter_num,
        'current_question': current_question,
        'current_index': current_index,
        'total_questions': total_questions,
        'total_1': total_1
    }
    return render(request, 'question/quiz.html', context)

@login_required
@csrf_exempt
def retest(request, chapter_num):
    current_user = request.user
    questions = SolvedQuestion.objects.filter(user=current_user, solved_questions__chapter=chapter_num, was_right=False)
    total_questions = questions.count()
    total_1 = total_questions - 1
    current_index = int(request.GET.get('q', 0))
    current_index = max(0, min(current_index, total_questions - 1))
    current_question = questions[current_index] if total_questions > 0 else None


    if request.method == 'POST':
        try:
            data = json.loads(request.body)
            submitted_answers = data.get('answers')

            if not current_user.is_authenticated:
                logger.warning("User not authenticated")
                return JsonResponse({'success': False, 'message': 'User not authenticated'}, status=401)

            total_correctness = 0
            for i, question in enumerate(questions):
                correctness = False
                if question.solved_questions.answer.lower() == submitted_answers[i].lower():
                    correctness = True
                    total_correctness += 1
                solved_question, created = SolvedQuestion.objects.get_or_create(
                    user=current_user,
                    solved_questions=question.solved_questions,
                    defaults={'was_right': correctness, 'submitted_answer': submitted_answers[i]}
                )
                if not created:
                    # If the solved question already exists, update it
                    solved_question.was_right = correctness
                    solved_question.submitted_answer = submitted_answers[i]
                    solved_question.save()
            exam_log = ExamLog(
                user=current_user,
                chapter=chapter_num,
                exam_dateTime=timezone.now(),
                total_solved_questions=total_questions,
                total_correct_questions=total_correctness
            )
            exam_log.save()

            request.session['correct_answers'] = total_correctness
            request.session['incorrect_answers'] = total_questions - total_correctness
            request.session['total_questions'] = total_questions
            request.session['chapter_num'] = chapter_num

            return JsonResponse({'success': True})
        except IntegrityError as e:
            logger.error("IntegrityError in quiz view: %s", str(e))
            return JsonResponse({'success': False, 'message': 'Integrity error occurred: ' + str(e)}, status=500)
        except Exception as e:
            logger.error("Error in quiz view: %s", str(e), exc_info=True)
            return JsonResponse({'success': False, 'message': str(e)}, status=500)

    # Render the retest template with the context
    context = {
        'chapter_num': chapter_num,
        'current_question': current_question,
        'current_index': current_index,
        'total_questions': total_questions,
        'total_1': total_1
    }
    return render(request, 'question/retest.html', context)

@login_required
def study(request, chapter_num):
    questions = Question.objects.filter(chapter=chapter_num)
    total_questions = questions.count()
    total_1 = total_questions - 1
    current_index = int(request.GET.get('q', 0))
    current_index = max(0, min(current_index, total_questions - 1))
    current_question = questions[current_index] if total_questions > 0 else None

    # Render the study template with the context
    context = {
        'chapter_num': chapter_num,
        'current_question': current_question,
        'current_index': current_index,
        'total_questions': total_questions,
        'total_1': total_1,
    }
    return render(request, 'question/study.html', context)

@login_required
def mistake_log(request):
    mistake_logs = ExamLog.objects.filter(user=request.user.id).order_by('-exam_dateTime')  # '-exam_dateTime' means that it is sorted by newest first.
    # Render the mistake log template with the exam logs
    return render(request, 'question/mistake_log.html', {"exam_logs": mistake_logs})

@login_required
def result(request):
    correct_answers = request.session.get('correct_answers', 0)
    incorrect_answers = request.session.get('incorrect_answers', 0)
    total_questions = request.session.get('total_questions', 0)
    chapter_num = request.session.get('chapter_num', 0)

    # Render the result template with the context
    context = {
        'correct_answers': correct_answers,
        'incorrect_answers': incorrect_answers,
        'total_questions': total_questions,
        'chapter_num': chapter_num,
    }

    return render(request, 'question/result.html', context)