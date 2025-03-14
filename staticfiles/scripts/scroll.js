document.addEventListener("DOMContentLoaded", function () {
    document.querySelectorAll("nav a").forEach(anchor => {
        anchor.addEventListener("click", function (event) {
            // Previne comportamentul standard
            event.preventDefault();

            const targetId = this.getAttribute("href").substring(1); // Extrage ID-ul
            const targetElement = document.getElementById(targetId); // Găsește elementul

            if (targetElement) {
                targetElement.scrollIntoView({
                    behavior: "smooth",
                    block: "start" // Asigură-te că secțiunea este plasată la începutul viewport-ului
                });
            }
        });
    });
});
