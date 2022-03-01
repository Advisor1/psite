//Header_fix
if($(window).width()>319){
  $(window).scroll(function () {
    var scroll = $(window).scrollTop();
    if (scroll >= 130) {
      $('header').addClass('fix_active');
    } else {
      $('header').removeClass('fix_active');
    }
  })
}

//menu-full
$(function(){
  $('a.mobile-trigger').on('click', function(){
      $('body').toggleClass('mobile-open');
  }) 

 $('.Fullmenu-bar .close_nav').on('click', function() {
    $('.Fullmenu-bar').removeClass('full_menu');
    $('body').removeClass('mobile-open');
  })
    
});

if($(window).width()<1024){
	  $('.sub-Menu-hov .mob-dd').addClass('dd-show');
	  $('.sub-Menu-hov .mob-dd').on('click', function(){
		  $(this).parents('.sub-Menu-hov').find('.sub-Menu').slideToggle();
		  $(this).toggleClass('dd-show');
	  })
}


$(document).click(function(e){
  if(!$(e.target).is('a.mobile-trigger, a.mobile-trigger *, .Fullmenu-bar, .Fullmenu-bar *')){
    $('.Fullmenu-bar').removeClass('full_menu');
    $('body').removeClass('mobile-open');
  }
});


