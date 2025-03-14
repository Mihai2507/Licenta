document.addEventListener("DOMContentLoaded", function () {
    const video1 = document.querySelector(".video1-container video");

    video1.addEventListener("timeupdate", function () {
        if (video1.duration - video1.currentTime <= 31) {
            video1.style.filter = "blur(10px)";
        }
    });
});
