document.addEventListener("DOMContentLoaded", function() {
    function fixButtons(selector) {
        let button = document.querySelector(selector);
        if (button) {
            let clone = button.cloneNode(true);
            button.replaceWith(clone);
        }
    }

    fixButtons("a[href*='signup']");
    fixButtons("a[href*='login']");
    fixButtons("a[href*='profil']");
});
