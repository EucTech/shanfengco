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
      url: '/messages_form/',
      data: formData,
      contentType: 'application/x-www-form-urlencoded',
      success: function (response, textStatus, xhr) {
        if (xhr.status === 200)
        console.log('Message sent successfully');
        $('#message').text(response.message).show();
        $('#myForm')[0].reset();
        $('#message-submit').val(submitvalue);
      },
      error: function (xhr, status, error) {
        console.error('Error:', error)
      },
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
      url: '/subscribe/',
      data: formData,
      contentType: 'application/x-www-form-urlencoded',
      success: function (response, textStatus, xhr) {
        if (xhr.status === 200){
          console.log('subscribed');
          $('#news-message').text(response.message).show();
          $('#mynewsletter')[0].reset();
          $('#em').hide();
          $('#newsletter-submit').val(submitvalue);
        }
      },
      error: function (xhr) {
        console.error('Error:', xhr.statusText);
        if (xhr.status === 400) {
          let responseJson = JSON.parse(xhr.responseText);
          $('#em').text(responseJson.message).show();
          $('#newsletter-submit').val(submitvalue);
        }
      },
    });
  });
});

