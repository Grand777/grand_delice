$(document).ready(function(){

	function _render() {
        var template = _.template($('#catalog-template').html()),
            $shopItems = $('.shopItems');
 
        $.getJSON('data/catalog.json', function(data) {
            $shopItems.html(template({shopItems: data}));
        });
    }

    _render();


    $('.close').on("click",function(){
    	$(this).closest('.modalWrapper').fadeOut(400);
    	$('.sizeSelectSpan').removeClass('activeSize');
    	$('.shopBoxSizeS-js').toggleClass('activeSize');
    	// $('.buyBtn').data('price', $('.activeSize').data('price'));
    });



    $('.shopItems').on("click", ".shopItem",function(){
		
		var id = $(this).data('id'),
		 	name = $(this).data('name'),
			price = $(this).data('prices'),
			img = $(this).data('img'),
			priceS = $(this).data('prices'),
			priceM = $(this).data('pricem'),
			priceL = $(this).data('pricel'),
			priceXL = $(this).data('pricexl');
		// console.log(priceS + " " + priceM + " " + priceL + " " + priceXL);

		$('.modalWrapper').fadeIn(1000);
		$('.modal_imgItem').attr('src', img);
		$('.info_head').html(name);
		$('.info_price').html(price + " грн");
		$('.shopBoxSizeS-js').attr('data-price', priceS);
		$('.shopBoxSizeM-js').attr('data-price', priceM);
		$('.shopBoxSizeL-js').attr('data-price',priceL);
		$('.shopBoxSizeXL-js').attr('data-price', priceXL);

		
		
		$('.buyBtn').attr('data-id', id)
		.attr('data-name', name)
		.attr('data-price', priceS)
		.attr('data-img', img);
	});



 });

