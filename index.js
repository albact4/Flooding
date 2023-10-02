/*Buttons code*/

document.addEventListener('DOMContentLoaded', () => {

    // Get the buttons by their IDs
    const learnButton = document.getElementById("learnButton");
    const redirectButton = document.getElementById("redirectButton");
    const explanationButton = document.getElementById("explanationButton");
    const redirectButton1 = document.getElementById("redirectButton1");
    const explanationButton1 = document.getElementById("explanationButton1");
  
    learnButton.addEventListener('click', () => {
      // Redirect to the desired HTML file
      window.location.href = 'about.html';
    });
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
  });
  
  