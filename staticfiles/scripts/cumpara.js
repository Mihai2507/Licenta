document.addEventListener("DOMContentLoaded", function () {
    const video3 = document.querySelector(".video3-container video");

    video3.addEventListener("timeupdate", function () {
        if (video3.duration - video3.currentTime <= 30) {
            video3.style.filter = "blur(10px)";
        }
    });
});
