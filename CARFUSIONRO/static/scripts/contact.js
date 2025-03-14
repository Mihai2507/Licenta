document.addEventListener("DOMContentLoaded", function () {
    const video4 = document.querySelector(".video4-container video");

    video4.addEventListener("timeupdate", function () {
        if (video4.duration - video4.currentTime <= 20) {
            video4.style.filter = "blur(10px)";
        }
    });
});
