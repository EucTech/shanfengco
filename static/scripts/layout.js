const navOpen = document.querySelector('.open');
const navClose = document.querySelector('.close');
const navlinksA = document.querySelectorAll('.navlinks a');
const navlinks = document.querySelector('.navlinks');

function OpenNav() {
    navlinks.style.top ="5em";
    navOpen.style.display = "none";
    navClose.style.display = "block";
}

function CloseNav() {
    navlinks.style.top ="-100em";
    navClose.style.display = "none";
    navOpen.style.display = "block";
}

navOpen.addEventListener('click', function() {
    OpenNav();
});

navClose.addEventListener('click', function() {
    CloseNav();
});

navlinksA.forEach(links => {
    links.addEventListener('click', function() {
        CloseNav();
    })
})


  // Get the button:
  let mybutton = document.getElementById("myBtn");

  // When the user scrolls down 20px from the top of the document, show the button
  window.onscroll = function() {scrollFunction()};
  
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
    document.body.scrollTo({ top: 0, behavior: 'smooth' }); // For Safari
    document.documentElement.scrollTo({ top: 0, behavior: 'smooth' }); // For Chrome, Firefox, IE and Opera
  }