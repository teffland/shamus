 // Adjust slider carousel to window width
$(resizeSlider);
$(window).resize(resizeSlider);

function resizeSlider (){
    var w = $(window).width();
    // console.log('Window Width = '+toString(w))
    $('.slide-image').width(w);
    // height is viewport - navbar (the whole thing fits on front)
    $('.slide-image').height($('html').height()-100);//(8.0/16.0) * w); //maintain 16:9
    // console.log('Adjusted Carousel');
};

// Manage Floating 'Top' menu link
// * Don't let it on to header
$('#top-link').scroll( function (){
    console.log(this.X());
});