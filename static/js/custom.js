$(document).ready(function () {
	$('.timepicker').timepicker({
		timeFormat: 'h:i a',
		interval: 60,
		defaultTime: '8',
		startTime: '00:00',
		dynamic: false,
		dropdown: true,
		scrollbar: true,
	});

	$('#like_btn').click(function () {
		let restaurantId;
		restaurantId = $(this).attr('data-restaurantid');

		jQuery.get(
			'/roadchillz/restaurants/like_restaurant/',
			{ restaurant_id: restaurantId },
			function (data) {
				$('#like_count').html(data);
				$('#like_btn').hide();
			}
		);
	});
});
