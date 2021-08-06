$( document ).ready(function() {
    $('.timepicker').timepicker({
        timeFormat: 'h:i a',
        interval: 60,
        defaultTime: '8',
        startTime: '00:00',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });
});
