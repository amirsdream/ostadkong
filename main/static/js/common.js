$(function strict() {
	'use strict';
	//Preloader fading out after site loading
	$( ".preloader" ).fadeOut("slow");

	//Div sizing for right margin-top working(DON'T REMOVE)
	$(".empty").css("min-height", $( ".head-bar" ).height());

	//Waves(Ripple) effect for these elements:
	Waves.attach('.malto-btn');
	Waves.attach('.malto-btn-flat');
	Waves.attach('.nav-tabs>li>a');
	Waves.init();

	//Mobile menu animation
	//Mobile menu toggle animation on icon click
    $(".material-icons").click(function(){
    	$('.mobile-menu').animate({width:'toggle'},350);
    });
	//Mobile menu toggle animation on menu-element click
	$(".mobile-menu .menu-element").click(function(){
		$('.mobile-menu').animate({width:'toggle'},350);
	});

	//Page scroll 2 id for these elements:
	$(".menu-element a").mPageScroll2id();
	$(".malto-btn a").mPageScroll2id();

	//Menu minimalization on scrolling
	function init() {
    	window.addEventListener('scroll', function(e){
        	var distanceY = window.pageYOffset || document.documentElement.scrollTop,
            	shrinkOn = 20,
            	header = document.querySelector(".head-bar");
        	if (distanceY > shrinkOn) {
				//Adding class .minimalized which is styled in CSS
            	classie.add(header, "minimalized");
        	} else {
            	if (classie.has(header, "minimalized")) {
                	classie.remove(header, "minimalized");
            	}
        	}
    	});
	}
	window.onload = init();


	//Owl carousel for 3 sections
	//For TEAM section
	$(".team-members").owlCarousel({
		//Autoscroll(in seconds)
		autoPlay: 8000,
		//Iems on the screen(in seconds)
		items : 4,
		itemsDesktop : [1199,4],
		itemsDesktopSmall : [992,3]
	});
	//For REVIEWS section
	$("#owl-review").owlCarousel({
		autoPlay: 8000,
		items : 3,
		itemsDesktop : [1920,1],
		itemsDesktopSmall : [973,1],
		itemsTablet : [768,1],
		itemsMobile	: [479,1]
	});
	//For PARTNERS section
	$(".images").owlCarousel({
		autoPlay: 8000,
		items : 4,
		itemsTablet : [768,2],
		itemsMobile	: [479,2]
	});

	//CONTACT FORM(Sending info to mail.php and alert "Thank you!")
	$("form").submit(function() {
	var th = $(this);
	$.ajax({
		type: "POST",
		url: "mail.php",
		data: th.serialize()
	}).done(function() {
		//You can write here the alert text
		alert("Thank you");
		setTimeout(function() {
			// Done Functions
			th.trigger("reset");
		}, 1000);
	});
	return false;
	});

	//Chrome Smooth Scroll
	try {
		$.browserSelector();
		if($("html").hasClass("chrome")) {
			$.smoothScroll();
		}
	} catch(err) {

	};

	$("img, a").on("dragstart", function(event) { event.preventDefault(); });
});
