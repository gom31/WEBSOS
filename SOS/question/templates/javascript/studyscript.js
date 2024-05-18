document.addEventListener('DOMContentLoaded', function () {
    // 사용자가 선택한 챕터를 가져오기 (예: URL 파라미터를 통해)
    const urlParams = new URLSearchParams(window.location.search);
    const chapter = urlParams.get('chapter') || '8'; // 기본값: 8

    // 챕터 타이틀 설정
    const chapterTitle = document.getElementById('chapter-title');
    chapterTitle.textContent = `Chapter ${chapter}`;

    // 애니메이션 활성화 클래스 추가
    setTimeout(() => {
        chapterTitle.classList.add('show');
    }, 100); // 페이지 로드 후 100ms 대기 후 애니메이션 시작

    // 문제 내용 설정 (데이터베이스에서 가져오는 로직 추가)
    const questionContent = document.getElementById('question-content');
    questionContent.textContent = `Question for Chapter ${chapter}`; // 예시 텍스트

    // 버튼 클릭 이벤트 설정
    document.getElementById('prev').addEventListener('click', () => {
        // 이전 문제로 이동하는 로직 추가
        alert('Previous Question');
    });

    document.getElementById('next').addEventListener('click', () => {
        // 다음 문제로 이동하는 로직 추가
        alert('Next Question');
    });
    
});
