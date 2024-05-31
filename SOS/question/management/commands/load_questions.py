import os
from django.core.management.base import BaseCommand
from django.core.files import File
from question.models import Question
from django.conf import settings

class Command(BaseCommand):
    help = 'Load questions into the database'

    def handle(self, *args, **kwargs):
        questions = [
            {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "allocation.png"),
             "answer": "allocation"},
            {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "assignment edge.png"),
             "answer": "assignment edge"},
            {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "available.png"),
             "answer": "available"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "banker's algorithm.png"),
             "answer": "banker's algorithm"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "circular wait.png"),
             "answer": "available"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "claim edge.png"),
             "answer": "claim edge"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "detection algorithm.png"),
             "answer": "detection algorithm"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "finish.png"),
             "answer": "finish"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "hold and wait.png"),
             "answer": "hold and wait"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "max.png"),
             "answer": "max"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "mutual exclusive.png"),
             "answer": "mutual exclusive"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "need.png"),
             "answer": "need"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "no preemption.png"),
             "answer": "no preemption"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "process termination.png"),
             "answer": "process termination"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "request edge.png"),
             "answer": "request edge"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "resource allocation graph.png"),
             "answer": "resource allocation graph"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "rollback.png"),
             "answer": "rollback"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "safe state.png"),
             "answer": "safe state"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "selecting a victim.png"),
             "answer": "selecting a victim"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "starvation.png"),
             "answer": "starvation"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "wait for graph.png"),
             "answer": "wait for graph"},
             {"chapter": 8,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter8", "work.png"),
             "answer": "work"},
             
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter9", "compile time.png"),
             "answer": "compile time"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter9", "load time.png"),
             "answer": "load time"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter9", "execution time.png"),
             "answer": "execution time"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter9", "memory management unit.png"),
             "answer": "memory management unit"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter9", "relocation register.png"),
             "answer": "relocation register"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter9", "dynamic loading.png"),
             "answer": "dynamic loading"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter9", "static linking.png"),
             "answer": "static linking"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter9", "contiguous allocation.png"),
             "answer": "contiguous allocation"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter9", "variable partition.png"),
             "answer": "variable partition"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter9", "hole.png"),
             "answer": "hole"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter9", "first fit.png"),
             "answer": "first fit"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter9", "best fit.png"),
             "answer": "best fit"},
             {"chapter": 9,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "chapter9", "best fit.png"),
             "answer": "worst fit"},


             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "6.png"),
             "answer": "a"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "7.png"),
             "answer": "b"},
             {"chapter": 10,
             "image": os.path.join(settings.BASE_DIR, "media", "quiz_images", "8.png"),
             "answer": "c"},
        ]
        for q in questions:
            if not Question.objects.filter(chapter=q["chapter"], answer=q["answer"]).exists():
                image_path = q["image"]
                if os.path.exists(image_path):
                    question = Question(
                        chapter=q["chapter"],
                        answer=q["answer"]
                    )
                    # 기존 파일을 참조
                    question.image.name = os.path.relpath(image_path, settings.MEDIA_ROOT)
                    question.save()
                    self.stdout.write(self.style.SUCCESS(f'Successfully loaded question: {q["answer"]}'))
                else:
                    self.stdout.write(self.style.ERROR(f'Image file not found: {image_path}'))
            else:
                self.stdout.write(self.style.WARNING(f'Skipping duplicated question: {q["answer"]}'))
        self.stdout.write(self.style.SUCCESS('Finished loading questions'))