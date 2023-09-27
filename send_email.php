<?php
if ($_SERVER["REQUEST_METHOD"] == "POST") {
    $to = "aclosatarres@wvstateu.edu"; // Replace with the recipient's email address
    $subject = "Contact Form Submission";
    
    $firstName = $_POST["firstName"];
    $lastName = $_POST["lastName"];
    $email = $_POST["email"];
    $mobileNumber = $_POST["mobileNumber"];
    $message = $_POST["message"];
    
    $messageBody = "First Name: $firstName\n";
    $messageBody .= "Last Name: $lastName\n";
    $messageBody .= "Email: $email\n";
    $messageBody .= "Mobile Number: $mobileNumber\n";
    $messageBody .= "Message:\n$message";
    
    // Additional headers
    $headers = "From: $email" . "\r\n" .
               "Reply-To: $email" . "\r\n" .
               "X-Mailer: PHP/" . phpversion();
    
    // Send the email
    mail($to, $subject, $messageBody, $headers);
    
    // Redirect back to the contact page or show a confirmation message
    header("Location: contact.html"); // Change this URL as needed
    exit();
}
?>
