var div_help = {
	init: function(){
		$('#help').click(this.call_details);
	},
	call_details: function(){
		var root = $(this).closest('.container');
		root.find('.big_div_help').show();
		root.find('.big_div_main_page').hide();
	}
}

var div_hello = {
	init: function(){
		$('#hello').click(this.call_details);
	},
	call_details: function(){
		var root = $(this).closest('.container');
		root.find('.big_div_hello').show();
		root.find('.big_div_main_page').hide();
	}
}

var div_uncomfortable = {
	init: function(){
		$('#uncomfortable').click(this.call_details);
	},
	call_details: function(){
		var root = $(this).closest('.container');
		root.find('.big_div_uncomfortable').show();
		root.find('.big_div_main_page').hide();
	}
}

var go_back = {
	init: function(){
		$('.restart').click(this.back_to_main);
	},
	back_to_main: function(){
		var root = $(this).closest('.container');
		root.find('.big_div_main_page').show();
		var big_div = $(this).parent().parent();
		big_div.hide();
	}
}

$('.boxes_cursor_pointer').click(function(){	
	var status = $(this).find('p').text().replace(/^\s*|\s*$/g,'');
	var snd = new Audio('');
	snd = new Audio('/static_media_alex/audio/'+status+'.mp3');
	snd.play();
	
});

div_help.init();
div_hello.init();
div_uncomfortable.init();
go_back.init();