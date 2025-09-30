let task5Map = null;
let task5LayerGroup = L.markerClusterGroup();

function initTask5() {
  const container = document.getElementById("map-task5");
  container.style.display = "block";
  container.offsetHeight;

  setTimeout(() => {
    task5Map = L.map("map-task5", {
      fadeAnimation: false,
      zoomAnimation: false,
      markerZoomAnimation: false,
    }).setView([59.324597639096226, 18.070971673722084], 10);

    document.getElementById("map-task5").classList.remove("leaflet-fade-anim");
    document.getElementById("l1").style.display = "none";

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(
      task5Map
    );

    fetch("../static/js/fuel.geojson")
      .then((res) => res.json())
      .then((data) => {
        data.features.forEach((feature) => {
          const coords = feature.geometry.coordinates;
          const latlng = [coords[1], coords[0]];
          const marker = L.marker(latlng);
          if (feature.properties?.name) {
            marker.bindPopup("<b>" + feature.properties.name + "</b>");
          }
          task5LayerGroup.addLayer(marker);
        });
        task5Map.addLayer(task5LayerGroup);
      });
  }, 100);
}

function clearTask5() {
  if (task5Map) {
    task5Map.remove();
    document.getElementById("map-task5").style.display = "none";
    task5Map = null;
    document.getElementById("l1").style.display = "none";
  }
}
