document.addEventListener('DOMContentLoaded', () => {
    const widgetToggle = document.getElementById('widget-toggle');
    const countdownContainer = document.getElementById('countdown-container');
    const thanksgivingCountdown = document.getElementById('thanksgiving-countdown');
    const christmasCountdown = document.getElementById('christmas-countdown');

                                             // change the dates and shit here//
    const thanksgivingBreak = new Date('February 17, 2025 9:30:00'); //countdown 1    
    const christmasBreak = new Date('May 28, 2025 12:30:00');   //countdown 2

    function updateCountdown() {
        const now = new Date();

        // countodwn 1
        const thanksgivingTimeLeft = thanksgivingBreak - now;
        if (thanksgivingTimeLeft > 0) {
            const thanksgivingDays = Math.floor(thanksgivingTimeLeft / (1000 * 60 * 60 * 24));
            const thanksgivingHours = Math.floor((thanksgivingTimeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const thanksgivingMinutes = Math.floor((thanksgivingTimeLeft % (1000 * 60 * 60)) / (1000 * 60));
            const thanksgivingSeconds = Math.floor((thanksgivingTimeLeft % (1000 * 60)) / 1000);
            thanksgivingCountdown.innerHTML = ` 🤵President’s day: ${thanksgivingDays}d ${thanksgivingHours}h ${thanksgivingMinutes}m ${thanksgivingSeconds}s left!`;
        } else {
            thanksgivingCountdown.innerHTML = " 🤵President’s day is here cuh on baby";
        }

        // countdown 2
        const christmasTimeLeft = christmasBreak - now;
        if (christmasTimeLeft > 0) {
            const christmasDays = Math.floor(christmasTimeLeft / (1000 * 60 * 60 * 24));
            const christmasHours = Math.floor((christmasTimeLeft % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
            const christmasMinutes = Math.floor((christmasTimeLeft % (1000 * 60 * 60)) / (1000 * 60));
            const christmasSeconds = Math.floor((christmasTimeLeft % (1000 * 60)) / 1000);
            christmasCountdown.innerHTML = `Last day of school🥺😭 ${christmasDays}d ${christmasHours}h ${christmasMinutes}m ${christmasSeconds}s left!`;
        } else {
            christmasCountdown.innerHTML = "Its summer ☀️😎 ";
        }
    }

    setInterval(updateCountdown, 1000);


    widgetToggle.addEventListener('click', () => {
        countdownContainer.classList.toggle('active');
    });
});

//© 2025 Math Realize. All rights reserved//
