$( document ).ready(function() {
    $('.timepicker').timepicker({
        timeFormat: 'h:mm p',
        interval: 60,
        defaultTime: '8',
        startTime: '00:00',
        dynamic: false,
        dropdown: true,
        scrollbar: true
    });
});

let map;

function initMap() {
  map = new google.maps.Map(document.getElementById("map"), {
    center: { lat: 55.8642, lng: -4.2518 },
    zoom: 10,
  });
}
