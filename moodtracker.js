var swiper = new Swiper(".slide-content", {
    slidesPerView: 2,
    spaceBetween: 25,
    centerSlide:'true',
    grabCursor:'true',
    pagination: {
      el: ".swiper-pagination",
      clickable: true,
      dynamicBullets: true,
    },
    navigation: {
      nextEl: ".swiper-button-next",
      prevEl: ".swiper-button-prev",
    },
  });

