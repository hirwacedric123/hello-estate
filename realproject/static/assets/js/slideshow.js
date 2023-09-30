'use strict'

let slideIndex = 0;
    
function showSlide(n) {
  const slides = document.querySelectorAll('.slide');
  slideIndex = (n + slides.length) % slides.length;

  slides.forEach(slide => {
    slide.style.display = 'none';
  });

  slides[slideIndex].style.display = 'block';
}

function nextSlide() {
  showSlide(slideIndex + 1);
}

// Show the first slide initially
showSlide(slideIndex);

// Automatically change slide every 4500 milliseconds (4.5 seconds)
setInterval(nextSlide, 4500);