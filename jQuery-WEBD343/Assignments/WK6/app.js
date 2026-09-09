$(function() {
  var $slides = $('#slider img');
  var current = 0;
  var animating = false;

  function showSlide(index) {
    if (animating || index === current) return;
    animating = true;

    var $currentSlide = $slides.eq(current);
    var $nextSlide    = $slides.eq(index);

    $currentSlide.removeClass('active');
    $nextSlide.addClass('active');

    setTimeout(function() {
      animating = false;
      current = index;
    }, 600);
  }

  $('#next').on('click', function() {
    showSlide((current + 1) % $slides.length);
  });

  $('#prev').on('click', function() {
    showSlide((current - 1 + $slides.length) % $slides.length);
  });

  setInterval(function() {
    showSlide((current + 1) % $slides.length);
  }, 5000);
});
