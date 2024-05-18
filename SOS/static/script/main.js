document.addEventListener('DOMContentLoaded', function() {
    var quizModal = document.getElementById("quizModal");
    var studyModal = document.getElementById("studyModal");
    var questionBtn = document.getElementById("questionBtn");
    var studyBtn = document.getElementById("studyBtn");
    var closeButtons = document.getElementsByClassName("close-button");
    var quizChapter8Btn = document.getElementById("quizChapter8Btn");
    var quizChapter9Btn = document.getElementById("quizChapter9Btn");
    var quizChapter10Btn = document.getElementById("quizChapter10Btn");
    var studyChapter8Btn = document.getElementById("studyChapter8Btn");
    var studyChapter9Btn = document.getElementById("studyChapter9Btn");
    var studyChapter10Btn = document.getElementById("studyChapter10Btn");

    // "Quiz" 버튼을 클릭하면 퀴즈 모달 창이 열립니다.
    questionBtn.onclick = function() {
        quizModal.style.display = "flex";
    }

    // "Study" 버튼을 클릭하면 학습 모달 창이 열립니다.
    studyBtn.onclick = function() {
        studyModal.style.display = "flex";
    }

    // 모달 창의 닫기 버튼(X)을 클릭하면 모달 창이 닫힙니다.
    Array.from(closeButtons).forEach(function(button) {
        button.onclick = function() {
            quizModal.style.display = "none";
            studyModal.style.display = "none";
        }
    });

    // 모달 외부를 클릭하면 모달 창이 닫힙니다.
    window.onclick = function(event) {
        if (event.target == quizModal) {
            quizModal.style.display = "none";
        }
        if (event.target == studyModal) {
            studyModal.style.display = "none";
        }
    }

    // Chapter 버튼 클릭 시 퀴즈 페이지로 이동
    quizChapter8Btn.onclick = function() {
        window.location.href = "/question/quiz/8/";
    }

    quizChapter9Btn.onclick = function() {
        window.location.href = "/question/quiz/9/";
    }

    quizChapter10Btn.onclick = function() {
        window.location.href = "/question/quiz/10/";
    }

    // Study 버튼 클릭 시 학습 페이지로 이동
    studyChapter8Btn.onclick = function() {
        window.location.href = "/question/study/8/";
    }

    studyChapter9Btn.onclick = function() {
        window.location.href = "/question/quiz/9/";
    }

    studyChapter10Btn.onclick = function() {
        window.location.href = "/question/quiz/10/";
    }

    // 이미지 컨테이너 마우스 움직임에 따른 효과
    var container = document.querySelector('.image-container');
    var overlay = document.querySelector('.overlay');

    container.addEventListener('mousemove', function(e) {
        var x = e.offsetX;
        var y = e.offsetY;
        var rotateY = -1 / 5 * x + 20;
        var rotateX = 4 / 30 * y - 20;

        overlay.style.backgroundPosition = `${x / 5 + y / 5}%`;
        overlay.style.filter = `opacity(${x / 200}) brightness(1.2)`;

        container.style.transform = `perspective(350px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
    });

    container.addEventListener('mouseout', function() {
        overlay.style.filter = 'opacity(0)';
        container.style.transform = 'perspective(350px) rotateY(0deg) rotateX(0deg)';
    });

});
