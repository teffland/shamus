 // Adjust slider carousel to window width
$(resizeSlider);
$(window).resize(resizeSlider);



function resizeSlider (){
    var w = $(window).width();
    console.log('Window Width = '+toString(w))
    $('.slide-image').width(w);
    $('.slide-image').height((9.0/16.0) * w); //maintain 16:9
    console.log('Adjusted Carousel');
};