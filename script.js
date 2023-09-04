/*
var gifs = document.getElementsByClassName("gif");
var displayButton = document.getElementById("displayButton");

//Function that hides gifs
function hideGifs() {
  for (var i = 0; i < gifs.length; i++) {
    gifs[i].style.display = "none";
  }
}
/* Function that shows the gif selected in the list
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
