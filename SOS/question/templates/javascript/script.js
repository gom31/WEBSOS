// 모달을 표시하는 함수
function showModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "block";
}

// 모달을 숨기는 함수
function hideModal() {
    var modal = document.getElementById("modal");
    modal.style.display = "none";
}

// 'Quiz' 버튼과 'Study' 버튼에 이벤트 리스너 추가
document.getElementById("questionBtn").addEventListener("click", function(event) {
    event.stopPropagation(); // 이벤트 전파를 막아 부모 요소에 영향을 주지 않도록 함
    showModal();
});

document.getElementById("studyBtn").addEventListener("click", function(event) {
    event.stopPropagation(); // 이벤트 전파를 막아 부모 요소에 영향을 주지 않도록 함
    showModal();
});

// 모달 닫기 버튼에 이벤트 리스너 추가
document.querySelector(".close-button").addEventListener("click", function() {
    hideModal();
});

// 모달 외부를 클릭하면 모달을 닫음
window.addEventListener("click", function(event) {
    var modal = document.getElementById("modal");
    if (event.target == modal) {
        hideModal();
    }
});




