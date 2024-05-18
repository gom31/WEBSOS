// 모달을 표시하는 함수
function showModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = "flex";
}

// 모달을 숨기는 함수
function hideModal(modalId) {
    var modal = document.getElementById(modalId);
    modal.style.display = "none";
}

// 'Quiz' 버튼에 이벤트 리스너 추가
document.getElementById("questionBtn").addEventListener("click", function(event) {
    event.stopPropagation(); // 이벤트 전파를 막아 부모 요소에 영향을 주지 않도록 함
    showModal("quizModal");
});

// 'Study' 버튼에 이벤트 리스너 추가
document.getElementById("studyBtn").addEventListener("click", function(event) {
    event.stopPropagation(); // 이벤트 전파를 막아 부모 요소에 영향을 주지 않도록 함
    showModal("studyModal");
});

// 모달 닫기 버튼에 이벤트 리스너 추가
document.querySelectorAll(".close-button").forEach(function(button) {
    button.addEventListener("click", function() {
        var modal = button.closest(".modal");
        modal.style.display = "none";
    });
});

// 모달 외부를 클릭하면 모달을 닫음
window.addEventListener("click", function(event) {
    if (event.target.classList.contains("modal")) {
        event.target.style.display = "none";
    }
});

// 각 챕터 버튼에 클릭 이벤트 추가 (Quiz)
document.getElementById("quizChapter8Btn").addEventListener("click", function() {
    window.location.href = "quiz.html?chapter_num=8";
});

document.getElementById("quizChapter9Btn").addEventListener("click", function() {
    window.location.href = "quiz.html?chapter_num=9";
});

document.getElementById("quizChapter10Btn").addEventListener("click", function() {
    window.location.href = "quiz.html?chapter_num=10";
});

// 각 챕터 버튼에 클릭 이벤트 추가 (Study)
document.getElementById("studyChapter8Btn").addEventListener("click", function() {
    window.location.href = "study.html?chapter_num=8";
});

document.getElementById("studyChapter9Btn").addEventListener("click", function() {
    window.location.href = "study.html?chapter_num=9";
});

document.getElementById("studyChapter10Btn").addEventListener("click", function() {
    window.location.href = "study.html?chapter_num=10";
});

// 이미지 3D 회전
var container = document.querySelector('.image-container');
var overlay = document.querySelector('.overlay');

container.addEventListener('mousemove', function(e) {
    var x = e.offsetX;
    var y = e.offsetY;
    var rotateY = -1/5 * x + 20;
    var rotateX = 4/30 * y - 20;

    overlay.style = `background-position: ${x/5 + y/5}%; filter: opacity(${x/200}) brightness(1.2)`;

    container.style = `transform: perspective(350px) rotateX(${rotateX}deg) rotateY(${rotateY}deg)`;
});

container.addEventListener('mouseout', function() {
    overlay.style = 'filter: opacity(0)';
    container.style = 'transform: perspective(350px) rotateY(0deg) rotateX(0deg)';
});

