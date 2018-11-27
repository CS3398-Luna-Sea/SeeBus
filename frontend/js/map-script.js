
var map;
function initMap() {
  map = new google.maps.Map(document.getElementById('map'), {
    zoom: 14,
    center: new google.maps.LatLng(29.8833, -97.9414),
    mapTypeId: 'roadmap'
  });

  image = 'http://seebus.net/images/Bus-icon.png';
  marker = new google.maps.Marker({ position: { lat: 29.8833, lng: -97.9414 }, map: map, icon: image});


  // marker.setMap(map);
}

// // Loop through the results array and place a marker for each
// // set of coordinates.
// window.eqfeed_callback = function (results) {
//   for (var i = 0; i < results.features.length; i++) {
//     var coords = results.features[i].geometry.coordinates;
//     var latLng = new google.maps.LatLng(coords[1], coords[0]);
//     var marker = new google.maps.Marker({
//       position: latLng,
//       map: map
//     });
//   }
// }
