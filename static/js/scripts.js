window.addEventListener('beforeunload', function () {
    sessionStorage.setItem('scrollPosition', window.scrollY);
});

window.addEventListener('load', function () {
    const scrollPosition = sessionStorage.getItem('scrollPosition');
    if (scrollPosition) {
        window.scrollTo({
            top: parseInt(scrollPosition, 10),
            left: 0,
            behavior: 'instant'
        });
        sessionStorage.removeItem('scrollPosition');
    }
});




