$(function(){
  var $box = $('#box');
  $box.css('border','4px solid #888');
  function animateBox(){
    $box
      .fadeOut(800)
      .fadeIn(800)
      .slideUp(800)
      .slideDown(800, animateBox);
  }
  animateBox();
});
