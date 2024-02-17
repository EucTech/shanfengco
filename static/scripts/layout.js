const navOpen = document.querySelector('.open');
const navClose = document.querySelector('.close');
const navlinksA = document.querySelectorAll('.navlinks a');
const navlinks = document.querySelector('.navlinks');

function OpenNav() {
  navlinks.style.top = "5em";
  navOpen.style.display = "none";
  navClose.style.display = "block";
}

function CloseNav() {
  navlinks.style.top = "-100em";
  navClose.style.display = "none";
  navOpen.style.display = "block";
}

navOpen.addEventListener('click', function () {
  OpenNav();
});

navClose.addEventListener('click', function () {
  CloseNav();
});

navlinksA.forEach(links => {
  links.addEventListener('click', function () {
    CloseNav();
  })
})


// Get the button:
let mybutton = document.getElementById("myBtn");

// When the user scrolls down 20px from the top of the document, show the button
window.onscroll = function () {
  scrollFunction()
};

function scrollFunction() {
  if (document.body.scrollTop > 60 || document.documentElement.scrollTop > 60) {
    mybutton.style.display = "block";
  } else {
    mybutton.style.display = "none";
  }
}

// When the user clicks on the button, scroll to the top of the document
function topFunction() {
  // Scroll to the top of the document smoothly
  document.body.scrollTo({
    top: 0,
    behavior: 'smooth'
  }); // For Safari
  document.documentElement.scrollTo({
    top: 0,
    behavior: 'smooth'
  }); // For Chrome, Firefox, IE and Opera
}

// To hide the messages after 5 seconds
// setTimeout(function () {
//   document.querySelectorAll('.messages').forEach(function (el) {
//     el.style.display = 'none';
//   });
// }, 5000);



// For message section

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


// For newsletter section

$(document).ready(function () {

  $('#mynewsletter').submit(function (event) {
    event.preventDefault();

    // get submit original value in html
    let submitvalue = $('#newsletter-submit').val();

    // set the value to loading when submiting
    $('#newsletter-submit').val('Loading.......');

    let formData = $(this).serialize();
    console.log(formData);

    $.ajax({
      type: 'POST',
      url: '/home/',
      data: formData,
      success: function (response) {
        console.log('subscribed');
        $('#news-message').text('Subscribed successfully!').show();
        $('#mynewsletter')[0].reset();
      },
      error: function (xhr, status, error) {
        console.error('Error:', error);
        console.log('Message sent error');
      },
      complete: function () {
        $('#newsletter-submit').val(submitvalue);
        // $('#mynewsletter')[0].reset();

      }
    });
  });


});

