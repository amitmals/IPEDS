


// -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------
//Use the lat/long of the Univ as the center and create a map
var latitudeSchool = 32.715736;
var longitudeSchool = -117.161087;
var nameSchool = "University of San Diego"
// ---------------------------------------------
var myMap = L.map("address-map", {
center: [latitudeSchool, longitudeSchool],
zoom:15
});
// Adding a tile layer (the background map image) to our map
// We use the addTo method to add objects to our map
L.tileLayer("https://api.tiles.mapbox.com/v4/{id}/{z}/{x}/{y}.png?access_token={accessToken}", {
attribution: "Map data &copy; <a href=\"https://www.openstreetmap.org/\">OpenStreetMap</a> contributors, <a href=\"https://creativecommons.org/licenses/by-sa/2.0/\">CC-BY-SA</a>, Imagery © <a href=\"https://www.mapbox.com/\">Mapbox</a>",
maxZoom: 18,
id: "mapbox.streets",
accessToken: API_KEY
}).addTo(myMap);

L.marker([latitudeSchool, longitudeSchool]).addTo(myMap)
   .bindPopup(nameSchool)
   .openPopup();
// -----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


  