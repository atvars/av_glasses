// Google Maps Functionality
        function initMap() {
            var map = new google.maps.Map(document.getElementById("map"), {
                zoom: 15,
                center: {
                    lat: 52.976849,
                    lng: -0.034810
                }
            });
            var labels = "ABCDEFGHIJKLMONPQRSTUVWXYZ";

            var locations = [{
                lat: 52.976849,
                lng: -0.034810
            }];

            var markers = locations.map(function(location, i) {
                return new google.maps.Marker ({
                    position: location,
                    label: labels[i % labels.length]
                });
            });

            var markerCluster = new MarkerClusterer(map, markers, {
                imagePath: 'https://developers.google.com/maps/documentation/javascript/examples/markerclusterer/m'
            });
        }
  

// for paragraph hover changing color
$(".hover").mouseenter(function(){
$(this).css("color", "blue");
});

$(".hover").mouseleave(function(){
$(this).css("color", "black");
});

// for title hover changing color
$(".name").mouseenter(function(){
$(this).css("color", "black");
});

$(".name").mouseleave(function(){
$(this).css("color", "green");
});


// shop now button animation
$(".shop-now-button").mouseenter(function(){
    $(this).animate({
      opacity: "1",
      height: "50px",
      width: "200px"
    });
  });
$(".shop-now-button").mouseleave(function(){
    $(this).animate({
      opacity: "1",
      height: "50px",
      width: "170px"
    });
  });

  // auto date in footer for copyrights
$("#copyright").text(new Date().getFullYear());