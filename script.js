var gifs = document.getElementsByClassName("gif");
var displayButton = document.getElementById("displayButton");

/* Function that hides gifs*/
function hideGifs() {
  for (var i = 0; i < gifs.length; i++) {
    gifs[i].style.display = "none";
  }
}
/* Function that shows the gif selected in the list*/
function showSelectedGif() {
  var selectedGif = document.getElementById(document.getElementById("gifSelector").value);
  hideGifs();
  selectedGif.style.display = "block";
}

/* Buttont that runs the function that displays the gif selected before*/
/*displayButton.addEventListener("click", showSelectedGif);


/*This JavaScript code is responsible for toggling the responsive behavior 
of the navigation bar when the hamburger icon is clicked.*/
function toggleNav() {
  var nav = document.getElementById("myTopnav");
  if (nav.className === "topnav") {
    nav.className += " responsive";
  } else {
    nav.className = "topnav";
  }
}



/*Buttons code*/
// Get the button element
const learnMoreButton = document.querySelector('.learn-more');

// Add click event listener to the button

learnMoreButton.addEventListener('click', () => {
  // Redirect to the desired HTML file
  window.location.href = 'about.html';
});




// Get the buttons by their IDs
const redirectButton = document.getElementById("redirectButton");
const explanationButton = document.getElementById("explanationButton");
const redirectButton1 = document.getElementById("redirectButton1");
const explanationButton1 = document.getElementById("explanationButton1");

// Add click event listeners to the buttons
redirectButton.addEventListener("click", () => {
  // Redirect to the desired page when the button is clicked
  window.location.href = "GoogleMaps.html";
});
redirectButton1.addEventListener("click", () => {
  // Redirect to the desired page when the button is clicked
  window.location.href = "hazard.html";
});

explanationButton.addEventListener("click", () => {
  // Redirect to another page when the button is clicked
  window.location.href = "about.html";
});
explanationButton1.addEventListener("click", () => {
  // Redirect to another page when the button is clicked
  window.location.href = "about.html";
});


