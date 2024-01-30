<?php
  $message_sent = false;

  if(isset($_POST['email']) && isset($_POST['email']) != '' )
  {

    if(filter_var($_POST['email'], FILTER_VALIDATE_EMAIL) ){
      // SUBMIT THE FORM
      $userFirstName = $_POST['firstName'];
      $userLastName = $_POST['lastName'];
      $userEmail = $_POST['email'];
      $userMobileNumber = $_POST['mobileNumber'];
      $message = $_POST['message'];


      $to = "aclosatarres@wvstateu.edu";
      $body = "";

      $body .= "From: ".$userFirstName;
      $body .= " ".$userLastName. "\r\n";
      $body .= "Email: ".$userEmail. "\r\n";
      $body .= "Mobile Number: ".$userMobileNumber. "\r\n";
      $body .= "Message: ".$message. "\r\n";

      mail($to, "New Contact Message from Website", $body);

      $message_sent = true;
    }
    else{
      $invalid_class_name = "form-invalid";
    }

  }

?>




<!DOCTYPE html>
<html lang="en">
<head>

  <meta charset="utf-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">

  <title>Contact Information</title>

  <!-- Link to favicon image -->
  <link rel="icon" type="image/x-icon" href="images\favicon.ico">
  
  <!-- Link to CSS file -->
  <link rel="stylesheet" href="styles.css">
  <link rel="stylesheet" href="https://fonts.googleapis.com/css?family=Open+Sans">
</head>
<body>



    <!-- Top Nav Menu -->
    <div class="topnav" id="myTopnav">
      <a href="https://www.wvstateu.edu/" class="logo">
          <img src="images\logo1.png" alt="Logo">
      </a>
      <a href="index.html" class="active">Home</a>
      <a href="GoogleMaps.html">Simulations</a>
      <a href="hazard.html">Hazard Zones</a>
      <a href="about.html">FAQs</a>
      <a href="contact.html">Contact</a>

      
      <i class="fa fa-bars"></i>
      </a>
    </div>


    <?php 

if( $message_sent):

?>

<h3> Thanks, we'll be in touch </h3>



<!-- is a PHP code block that is used to check if the message has not been sent successfully. If the
message has not been sent, it displays the contact form. This code block is used in conjunction with
the `if( )` code block to control the flow of the page based on whether the message has
been sent or not. -->
<?php 
else:
?>

<section id="mySection">

<div class="contact_container">
    
  <div class="contactInfo"> 
      <div>
          <!-- Header -->
          <h2>Contact Information</h2>
          
          <ul class="info">
            <li>
              <span><img src="images\iconmonstr-location-1-240.png"></span>
              <span>  P.O. Box 1000 <br>Institute, WV 25112-1000 </span>
            </li>
            <li>
              <span><img src=" images\iconmonstr-gmail-1-240 (1).png"></span>
              <span>  Alba Closa Tarres (Project leader)
                <br><a href="mailto:aclosatarres@wvstateu.edu">aclosatarres@wvstateu.edu</a> </span>                
            </li>
            <li>
              <span><img src=" images\iconmonstr-gmail-1-240 (1).png"></span>
              <span>  Fernando Rojano (Supervisor)
                <br><a href="mailto:fernando.rojano@wvstateu.edu">fernando.rojano@wvstateu.edu</a> </span>
            </li>
          </ul>
      </div>
    </div>

    <div class="contactForm"> 
      <h2>Send a Message</h2>
      <form action="contact.php" method="POST" class="form">
        <div class="formBox">
          <div class="inputBox w50">
            <label for="firstName">First Name</label>
            <input type="text" id="firstName" name="firstName" required placeholder="First Name">
          </div>
          <div class="inputBox w50">
            <label for="lastName">Last Name</label>
            <input type="text" id="lastName" name="lastName" required placeholder="Last Name">
          </div>
          <div class="inputBox w50">
            <label for="email">Email Address</label>
            <input type="email" id="email" name="email" required  placeholder="Email Address">
          </div>
          <div class="inputBox w50">
            <label for="mobileNumber">Mobile Number</label>
            <input type="text" id="mobileNumber" name="mobileNumber" required placeholder="Mobile Number">
          </div>
          <div class="inputBox w100">
            <label for="message">Write your Message...</label>
            <textarea id="message" name="message" required placeholder="Write your Message..."></textarea>
          </div>
          <div class="inputBox w100">
            <button>
              <span>Send</span>
            </button>
          </div>
        </div>
      </form>
    </div>
    
</div>
</section>



<!-- Is used to close the if statement in PHP. In this code, it is used to close
the if statement that checks if the message has been sent successfully. If the message has been
sent, it displays a "Thanks, we'll be in touch" message. If the message has not been sent, it
displays the contact form. -->
<?php 
  endif;
?>




<div class="bottom">
  <img src="images\logo1.png" alt="logob" class="logo">
</div>


  <script src="script.js"></script>
  <script src="https://smtpjs.com/v3/smtp.js"></script>
  <script> 

    // Add an event listener when the DOM (document) is fully loaded
    document.addEventListener('DOMContentLoaded', function() {
    // Select all input and textarea fields on the page
    const inputFields = document.querySelectorAll('input, textarea');

    // Loop through each input and textarea field
    inputFields.forEach(field => {
      // Add an event listener to each field for input events (typing)
      field.addEventListener('input', function() {
        // Find the label associated with the current field
        const label = this.parentElement.querySelector('label');

        // Check if the field's value is not empty
        if (this.value !== '') {
          // If the field is not empty, change the label's text color to a lighter color
          label.style.color = "#f2f2f2"; // Use style.color to change label color
        } else {
          // If the field is empty, change the label's text color back to its original color
          label.style.color = "#333"; // Use style.color to change label color
        }
      });
    });
  });


  </script>
  
</body>
</html>
