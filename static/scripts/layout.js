const navOpen = document.querySelector('.open');
const navClose = document.querySelector('.close');
const navlinksA = document.querySelectorAll('.navlinks a');
const navlinks = document.querySelector('.navlinks');

function OpenNav() {
    navlinks.style.top ="4em";
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