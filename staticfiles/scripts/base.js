document.addEventListener("DOMContentLoaded", function() {
    const urlParams = new URLSearchParams(window.location.search);
    const section = urlParams.get("scroll");

    if (section) {
        const targetElement = document.getElementById(section);
        if (targetElement) {
            setTimeout(() => {
                targetElement.scrollIntoView({ behavior: "smooth" });
            }, 500); // Așteaptă puțin pentru a evita probleme de încărcare
        }
    }
});
