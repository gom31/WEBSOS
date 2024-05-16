// 드롭다운 메뉴를 표시하고 숨기는 함수
function toggleDropdown(dropdownId) {
    var dropdowns = document.getElementsByClassName("dropdown-content");
    for (var i = 0; i < dropdowns.length; i++) {
        if (dropdowns[i].id !== dropdownId) {
            dropdowns[i].style.display = "none"; // 다른 메뉴 숨기기
        }
    }
    var dropdown = document.getElementById(dropdownId);
    if (dropdown.style.display === "none" || dropdown.style.display === "") {
        dropdown.style.display = "block";
    } else {
        dropdown.style.display = "none";
    }
}

// 'Question' 버튼과 'Study' 버튼에 이벤트 리스너 추가
document.getElementById("questionBtn").addEventListener("click", function() {
    toggleDropdown("dropdownMenuQuestion");
});

document.getElementById("studyBtn").addEventListener("click", function() {
    toggleDropdown("dropdownMenuStudy");
});

// 클릭 시 드롭다운 메뉴를 닫는 기능 추가
window.addEventListener("click", function(event) {
    if (!event.target.matches('.gradient-button')) {
        var dropdowns = document.getElementsByClassName("dropdown-content");
        for (var i = 0; i < dropdowns.length; i++) {
            var openDropdown = dropdowns[i];
            if (openDropdown.style.display === "block") {
                openDropdown.style.display = "none";
            }
        }
    }
});
