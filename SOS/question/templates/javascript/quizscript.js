document.addEventListener('DOMContentLoaded', function () {
    // Chapter 8 타이틀 요소 가져오기
    const chapterTitle = document.querySelector('.chapter-title');
    
    // 애니메이션 활성화 클래스 추가
    setTimeout(() => {
        chapterTitle.classList.add('show');
    }, 500); // 페이지 로드 후 500ms 대기 후 애니메이션 시작
});