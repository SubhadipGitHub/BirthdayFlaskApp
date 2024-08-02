// Set the date we're counting down to
var countDownDate = new Date("Aug 2, 2024 00:00:00").getTime();

var message = "Happy Birthday Rim ,to the most wonderful person in my life. You light up my world and make every day special. I love you more than words can express.";
var gif_url = "https://media.tenor.com/DhFPo_LQGt4AAAAj/alice-sticker-alice-animated.gif";

// Update the count down every 1 second
var x = setInterval(function() {

  // Get today's date and time
  var now = new Date().getTime();

  // Find the distance between now and the count down date
  var distance = countDownDate - now;

  // Time calculations for days, hours, minutes and seconds
  var days = Math.floor(distance / (1000 * 60 * 60 * 24));
  var hours = Math.floor((distance % (1000 * 60 * 60 * 24)) / (1000 * 60 * 60));
  var minutes = Math.floor((distance % (1000 * 60 * 60)) / (1000 * 60));
  var seconds = Math.floor((distance % (1000 * 60)) / 1000);

  // Display the result in the element with id="countdown"
  document.getElementById("countdown").innerHTML = `
    <div>${days}<span> Days</span></div>
    <div>${hours}<span> Hours</span></div>
    <div>${minutes}<span> Minutes</span></div>
    <div>${seconds}<span> Seconds</span></div>
  `;

  // If the count down is finished, replace the countdown with the birthday message
  if (distance < 0) {
    clearInterval(x);
    var countdownWrapper = document.getElementById('countdown-wrapper');
    var birthdayWrapper = document.getElementById('birthday-wrapper');
    var birthdayMessage = document.getElementById('birthday-message');

    birthdayMessage.innerHTML = `
      <p>${message}</p>
      <img src="${gif_url}" alt="Birthday Gif">
    `;

    countdownWrapper.style.opacity = '0';
    setTimeout(function() {
      countdownWrapper.style.display = 'none';
      birthdayWrapper.style.display = 'block';
      setTimeout(function() {
        birthdayWrapper.style.opacity = '1';
      }, 50);
    }, 1500); // Match the transition duration
  }
}, 1000);
