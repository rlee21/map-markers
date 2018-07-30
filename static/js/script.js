// document.addEventListener("DOMContentLoaded", function(){
//   if (document.querySelectorAll("#map").length > 0)
//   {
//     var js_file = document.createElement("script");
//     js_file.type = "text/javascript";
//     js_file.src = "https://maps.googleapis.com/maps/api/js?key=API_KEY&callback=initMap";
//     document.getElementsByTagName("head")[0].appendChild(js_file);
//   }
// });
 // function initMap(){
 //   var options = {
 //       center: {lat: 39.8283, lng: -98.5795},
 //       zoom: 4.5
 //   };
 //   var map = new google.maps.Map(document.getElementById("map"), options);
 //   var markers = {{ markers|tojson }};
 //   for(var i = 0; i < markers.length; i ++){
 //       addMarker(markers[i]);
 //   };
 //   function addMarker(props){
 //       var marker = new google.maps.Marker({
 //           position: props.coords,
 //           map: map
 //           });
 //       if (props.content){
 //           var infoWindow = new google.maps.InfoWindow({
 //               content: props.content
 //           });
 //           marker.addListener("click", function(){
 //               infoWindow.open(map, marker);
 //           });
 //       };
 //   };
 // };

