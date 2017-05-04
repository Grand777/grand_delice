$(document).ready(function(){


    // function _render() {
    //     var template = _.template($('#catalog-template').html()),
    //         $shopItems = $('.shopItems');
    //
    //     $.getJSON('data/catalog.json', function(data) {
    //         $shopItems.html(template({shopItems: data}));
    //     });
    // }
    //
    // _render();
    $('.close').click(function(){
    	$(this).closest('.modalWrapper').fadeOut(400);
    });



    $('.shopItems').on("click", ".shopItem",function(){
		
		var id = $(this).data('id');
		var name = $(this).data('name');
		var price = $(this).data('price');
		var img = $(this).data('img');

		$('.modalWrapper').fadeIn(1000);

		$('.modal_imgItem').attr('src', img);
		
		$('.buyBtn').attr('data-id', id)
		.attr('data-name', name)
		.attr('data-price', price)
		.attr('data-img', img);
	});



 });

