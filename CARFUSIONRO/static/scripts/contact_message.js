window.onload = function() {
    const urlParams = new URLSearchParams(window.location.search);
    const scrollTo = urlParams.get('scroll_to');

    if (scrollTo === 'video4') {
        const section = document.getElementById('video4');
        if (section) {
            section.scrollIntoView({ behavior: 'smooth' });
        }
        const notification = document.getElementById('notification');
        if (notification) {
            notification.style.display = 'block';
        }
        setTimeout(function() {
            if (notification) {
                notification.style.display = 'none';
            }
        }, 20000);
    }
}
