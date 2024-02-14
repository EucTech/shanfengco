$(document).ready(function () {
    $('#myForm').submit(function (event) {
      event.preventDefault();
  
      // get submit original value in html
      let submitvalue = $('#message-submit').val();
  
      // set the value to loading when submiting
      $('#message-submit').val('Loading.......');
  
      let formData = $(this).serialize();
      console.log(formData);
  
      $.ajax({
        type: 'POST',
        url: '/home/',
        data: formData,
        success: function (response) {
          console.log('Message sent successfully');
          $('#message').text('Your message has been sent successfully!').show();
          // Clear form values
          $('#myForm')[0].reset();
        },
        error: function (xhr, status, error) {
          console.error('Error:', error)
        },
        complete: function () {
          $('#message-submit').val(submitvalue);
        }
      });
    });
  });