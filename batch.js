document.addEventListener("DOMContentLoaded", function() {
    const runButton = document.getElementById("runButton");
    const loader = document.getElementById("loader");
    const output = document.getElementById("output");

    runButton.addEventListener("click", function() {
        // Show the loader and hide the button
        loader.style.display = "block";
        runButton.style.display = "none";

        // Make an AJAX request to execute the batch file
        fetch("C:\Users\Rojano\Documents\GitHub\Flooding\execute_batch.php") // Replace with the actual server-side script
            .then(response => response.text())
            .then(data => {
                // Hide the loader and display the result
                loader.style.display = "none";
                output.innerText = data;
            })
            .catch(error => {
                // Handle any errors here
                console.error("Error:", error);
            });
    });
});
