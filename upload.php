<?php
if (isset($_POST['submit'])) {
    $uploadDir = 'uploads'; // Directory to store uploaded files

    // Check if the file was uploaded without errors
    if ($_FILES['file']['error'] === UPLOAD_ERR_OK) {
        $tempFile = $_FILES['file']['tmp_name'];
        $targetFile = $uploadDir . $_FILES['file']['name'];

        // Move the uploaded file to the target directory
        if (move_uploaded_file($tempFile, $targetFile)) {
            echo "File uploaded successfully.";
        } else {
            echo "Error uploading file.";
        }
    } else {
        echo "File upload error: " . $_FILES['file']['error'];
    }
}
?>
