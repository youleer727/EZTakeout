"use strict";

angular.module('ezTakeoutApp').controller('MapCtrl', function MapCtrl($scope) {
  var map_loaded = false;
  var yelp_loaded = false;
  var long = null;
  var lat = null;
  var yelp_data = {};
  var map = null;
  var pathArray = location.href.split("/");
  var url = pathArray[0] + "//" + pathArray[2];
  var POST_baseurl = url + "/";
  // since expecting costly operaion, show loading first
  $(document).ready(function() {
    reveal("loading");
  });

  if (navigator.geolocation) {
    navigator.geolocation.getCurrentPosition(function(position) {
      lat = position.coords.latitude;
      long = position.coords.longitude;
      getYelpAndMap();
    }, function() {
      getIpFromBackend();
    });
  } else {
    console.log("geo function is disabled");
    getIpFromBackend();
  }

  function getIpFromBackend() {
    $.ajax({
      type: "POST",
      success: function(response) {
        var error = response.error;
        if (error) {
          reveal(error);
          $("#error-msg").text("ip lookup failed");
        } else {
          lat = response.lat;
          long = response.long;
          getYelpAndMap();
        }
      },
      error: function(xhr) {
        console.log(xhr);
      },
      url: POST_baseurl + "ip"
    });
  }


  function getYelpAndMap() {
    var today = new Date();
    $.ajax({
      type: "POST",
      data: {
        "month": today.getMonth(),
        "day": today.getDate(),
        "hour": today.getHours(),
        "time_range": getAttributes("time", window.location.href),
        "food_type": getAttributes("type", window.location.href),
        "cost_range": getAttributes("cost", window.location.href),
        "geolocation": false,
        "long": long,
        "lat": lat,
        "radius": 1000,
        "limit": 10
      },
      success: function(response) {
        YelpCallback(response);
      },
      error: function(xhr) {
        console.log("backend Yelp call failed");
        console.log(xhr);
      },
      url: POST_baseurl + "yelp"
    });
    mapboxgl.accessToken = "pk.eyJ1IjoieWxxaWFvMTM0MSIsImEiOiJjamI4bnEwdXcwN2hhMzNxcXhmb2xxaWVsIn0.cXxo1gK3catZKtPykP5_7g";
    map = new mapboxgl.Map({
      container: "map",
      style: "mapbox://styles/ylqiao1341/cjb8nqfz93n1r2rnqz0e0lfvg",
      center: [long, lat],
      zoom: 15
    });
    map.on("load", function(e) {
      MapCallback(e);
    });
  }


  function YelpCallback(data) {
    yelp_loaded = true;
    yelp_data = data;
    console.log(data);
    if (map_loaded) {
      revealMap();
    } else {
      console.log("map not loaded");
    }
  }

  function MapCallback(e) {
    map_loaded = true;
    if (yelp_loaded) {
      revealMap();
    } else {
      console.log("yelp not loaded");
    }
  }

  function revealMap() {
    reveal("loaded");
    var data = yelp_data;
    console.log("data: ");
    console.log(data);
    if (data.length === 0) {
      ZeroResults();
    } else {
      var listings = document.getElementById("listings");
      for (var i = 0; i < data.length; i += 1) {
        var parent_div = listings.appendChild(document.createElement('a'));
        parent_div.href = "javascript:;";
        parent_div.className = 'title';
        parent_div.dataPosition = i;
        parent_div.innerHTML = "";
        var name = data[i].name;
        var listing = parent_div.appendChild(document.createElement("div"));
        listing.className = "item";
        listing.id = "listing-" + i;
        var details = listing.appendChild(document.createElement("div"));
        details.innerHTML = "<h4>" + name + "</h4>";
        var rating_div = listing.appendChild(document.createElement("div"));
        rating_div.innerHTML += "Rating: ";
        for (var j = 0; j < Math.round(data[i].rating); j++) {
          rating_div.innerHTML += "⭐️";
        }
        rating_div.innerHTML = "<h6>" + rating_div.innerHTML + "</h6>";
        parent_div.addEventListener('click', function(e) {
          var clickedListing = data[this.dataPosition];
          flyToStore(clickedListing, true);
          createPopUp(clickedListing, true);
          var activeItem = document.getElementsByClassName('active');
          if (activeItem[0]) {
            activeItem[0].classList.remove('active');
          }
          this.parentNode.classList.add('active');
        });
      }

      var features = [];

      for (var i = 0; i < data.length; i += 1) {
        var address = data[i].location.display_address[0] + ", " + data[i].location.display_address[1];
        var current_listing = data[i];
        features.push({
          "type": "Feature",
          "geometry": {
            "type": "Point",
            "coordinates": [current_listing.coordinates.longitude, current_listing.coordinates.latitude]
          },
          "properties": {
            "title": current_listing.name,
            "icon-image": "restaurant-15",
            "address": address
          }
        });
      }
      map.addLayer({
        "id": "locations",
        "type": "symbol",
        "source": {
          "type": "geojson",
          "data": {
            "type": "FeatureCollection",
            "features": features
          }
        },
        "layout": {
          "icon-image": "{icon}-15",
          "text-field": "{title}",
          "text-font": ["Open Sans Semibold", "Arial Unicode MS Bold"],
          "text-offset": [0, 0.6],
          "text-anchor": "top"
        }
      });
      map.on('click', function(e) {
        var features = map.queryRenderedFeatures(e.point, {
          layers: ['locations']
        });
        if (features.length) {
          var clickedPoint = features[0];
          flyToStore(clickedPoint, false);
          createPopUp(clickedPoint, false);
          var activeItem = document.getElementsByClassName('active');
          if (activeItem[0]) {
            activeItem[0].classList.remove('active');
          }
          var selectedFeature = clickedPoint.properties.address;
        }
      });
    }
  }
  function ZeroResults() {
    reveal("zero-results");
  }
  function flyToStore(currentFeature, listing_src) {
    if (listing_src) {
      map.flyTo({
        center: [currentFeature.coordinates.longitude, currentFeature.coordinates.latitude],
        zoom: 14
      });
    } else {
      map.flyTo({
        center: currentFeature.geometry.coordinates,
        zoom: 14
      });
    }

  }

  function createPopUp(currentFeature, listing_src) {

    if (listing_src) {
      console.log(currentFeature);
      var popUps = document.getElementsByClassName('mapboxgl-popup');
      if (popUps[0]) {
        popUps[0].remove();
      }
      var popup = new mapboxgl.Popup({
          closeOnClick: true
        })
        .setLngLat([currentFeature.coordinates.longitude, currentFeature.coordinates.latitude])
        .setHTML('<h3>' + currentFeature.name + '</h3>' +
          "<a href='https://www.google.com/maps/place/" +
          currentFeature.location.display_address[0] + ", " + currentFeature.location.display_address[1] + "'>" +
          '<h4>' + currentFeature.location.display_address[0] + ", " + currentFeature.location.display_address[1] + '</h4></a>'
        )
        .addTo(map);
    } else {
      console.log(currentFeature);
      var popUps = document.getElementsByClassName('mapboxgl-popup');
      if (popUps[0]) { popUps[0].remove(); }
      console.log(currentFeature.properties.address)
      var popup = new mapboxgl.Popup({
          closeOnClick: true
        })
        .setLngLat(currentFeature.geometry.coordinates)
        .setHTML('<h3>' + currentFeature.properties.title + '</h3>' +
          "<a href='https://www.google.com/maps/place/" + currentFeature.properties.address + "'>" +
          '<h4>' + currentFeature.properties.address + '</h4></a>')
        .addTo(map);
    }

  }

  function reveal(name) {
    var divs = ["loaded", "loading", "zero-results", "error"]
    for (var i = 0; i < divs.length; i += 1) {
      $("#" + divs[i]).hide();
    }
    $("#" + name).show();
  }

  function getAttributes(name, url) {
    if (!url) {
      url = window.location.href;
    }
    name = name.replace(/[\[\]]/g, "\\$&");
    var regex = new RegExp("[?&]" + name + "(=([^&#]*)|&|#|$)"), res = regex.exec(url);
    if (!res) return null;
    if (!res[2]) return "";
    return decodeURIComponent(res[2].replace(/\+/g, " "));
  }
});
