$(".testimonies .quotes").owlCarousel({
    items: 3,
    loop: true,
    autoplay: true,
    margin: 50,
    dots: true,
    arrows: true,
    nav: false,
    navText: ["<i class='fa fa-chevron-left'></i>", "<i class='fa fa-chevron-right'></i>"],
    responsive: {
      0: {
        items: 1,
        nav: true,
        loop: true,
      },
      700: {
        items: 2,
        nav: true,
        loop: true,
      },
      800: {
          items: 2,
          nav: true,
          loop: true,
        },
      1200: {
        items: 3,
        nav: true,
        loop: true,
      },
    },
  });


  $(".works .main").owlCarousel({
    items: 3,
    loop: true,
    autoplay: true,
    margin: 50,
    // dots: true,
    arrows: true,
    nav: false,
    navText: ["<i class='fa fa-chevron-left'></i>", "<i class='fa fa-chevron-right'></i>"],
    responsive: {
      0: {
        items: 1,
        nav: true,
        loop: true,
      },
      700: {
        items: 2,
        nav: true,
        loop: true,
      },
      800: {
          items: 2,
          nav: true,
          loop: true,
        },
      1200: {
        items: 3,
        nav: true,
        loop: true,
      },
    },
  });