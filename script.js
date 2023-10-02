
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
