document.addEventListener("DOMContentLoaded", function () {
    const video2 = document.querySelector(".video2-container video");

    video2.addEventListener("timeupdate", function () {
        if (video2.duration - video2.currentTime <= 40) {
            video2.style.filter = "blur(10px)";
        }
    });
});
