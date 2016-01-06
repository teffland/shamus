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

// Add slideDown animation to dropdown
$('.dropdown').on('show.bs.dropdown', function(e){
  $(this).find('.dropdown-menu').first().stop(true, true).slideDown();
});

// Add slideUp animation to dropdown
$('.dropdown').on('hide.bs.dropdown', function(e){
  $(this).find('.dropdown-menu').first().stop(true, true).slideUp();
});

// Sticky header for style
// $(window).scroll(function() {
// if ($(this).scrollTop() > 10){  
//     $('div.nav-container').removeClass("nav-container").addClass("nav-container-sticky");
//   }
//   else{
//     $('div.nav-container-sticky').removeClass("nav-container-sticky").addClass("nav-container");
//   }
// });