$(document).ready(function(){
	console.log('ready');
	var contador = 1;
	$('.bt-menu').click(function(e){
				// $('nav').toggle(); 
		  e.preventDefault();
		if(contador == 1){
			$('nav').animate({
				left: '0'
			});
			contador = 0;
		}else {
			contador = 1;
			$('nav').animate({
				left: '-100%'
			});
		}
	});

	var i = 0;

	
	var control = setInterval(cambiarSlider, 3000);

	function cambiarSlider(){
		i++;
		if(i == $(".lared img").size()){
			i = 0;
		}
		$(".lared img").hide();
		$(".lared img").eq(i).fadeIn("medium");
	}


	var j = 0;
	var control2 = setInterval(cambiarSlider2, 3000);

	function cambiarSlider2(){
		j++;
		if(j == $(".votaciones img").size()){
			j = 0;
		}
		$(".votaciones img").hide();
		$(".votaciones img").eq(j).fadeIn("medium");
	}

	var h = 0;
	var control3 = setInterval(cambiarSlider3, 3000);

	function cambiarSlider3(){
		h++;
		if(h == $(".prestamos img").size()){
			h = 0;
		}
		$(".prestamos img").hide();
		$(".prestamos img").eq(h).fadeIn("medium");
	}

	var c = 0;
	var control4 = setInterval(cambiarSlider4, 3000);

	function cambiarSlider4(){
		c++;
		if(c == $(".clinica img").size()){
			c = 0;
		}
		$(".clinica img").hide();
		$(".clinica img").eq(c).fadeIn("medium");
	}

});/*fin document*/
		