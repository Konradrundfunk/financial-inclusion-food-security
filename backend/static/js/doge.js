var map = new ol.Map({
  target: 'map',
  layers: [
    new ol.layer.Tile({
        source: new ol.source.OSM()
    })
  ],
    view: new ol.View({
    center: ol.proj.fromLonLat([0, 0]),
    zoom: 2
  })
});


function onCountryMouseOut(e){
	C.geojson.resetStyle(e.target);
//	$("#countryHighlighted").text("No selection");

	var countryName = e.target.feature.properties.name;
	var countryCode = e.target.feature.properties.iso_a2;
//callback when mouse exits a country polygon goes here, for additional actions
}

/**
 * Callback for when a country is clicked. Will take care of the ui aspects, and it will call
 * other callbacks when done
 * @param e
 */
function onCountryClick(e){
//callback for clicking inside a polygon
}

/**
 * Callback for when a country is highlighted. Will take care of the ui aspects, and it will call
 * other callbacks after done.
 * @param e
 */
function onCountryHighLight(e){
	var layer = e.target;

	layer.setStyle({
		weight: 2,
		color: '#666',
		dashArray: '',
		fillOpacity: 0.7
	});

	if (!L.Browser.ie && !L.Browser.opera) {
		layer.bringToFront();
	}

	var countryName = e.target.feature.properties.name;
	var countryCode = e.target.feature.properties.iso_a2;
//callback when mouse enters a country polygon goes here, for additional actions
}

/**
 * Callback for mouse out of the country border. Will take care of the ui aspects, and will call
 * other callbacks after done.
 * @param e the event
 */
 function onCountryMouseOut(e){
	C.geojson.resetStyle(e.target);
//	$("#countryHighlighted").text("No selection");

	var countryName = e.target.feature.properties.name;
	var countryCode = e.target.feature.properties.iso_a2;
//callback when mouse exits a country polygon goes here, for additional actions
}

/**
 * Callback for when a country is clicked. Will take care of the ui aspects, and it will call
 * other callbacks when done
 * @param e
 */
function onCountryClick(e){
//callback for clicking inside a polygon
}

/**
 * Callback for when a country is highlighted. Will take care of the ui aspects, and it will call
 * other callbacks after done.
 * @param e
 */
function onCountryHighLight(e){
	var layer = e.target;

	layer.setStyle({
		weight: 2,
		color: '#666',
		dashArray: '',
		fillOpacity: 0.7
	});

	if (!L.Browser.ie && !L.Browser.opera) {
		layer.bringToFront();
	}

	var countryName = e.target.feature.properties.name;
	var countryCode = e.target.feature.properties.iso_a2;
//callback when mouse enters a country polygon goes here, for additional actions
}