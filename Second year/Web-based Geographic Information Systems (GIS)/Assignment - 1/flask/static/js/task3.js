let task3Map = null;

function initTask3() {
  const container = document.getElementById("map-task3");
  container.style.display = "block";
  container.offsetHeight;

  setTimeout(() => {
    task3Map = L.map("map-task3", {
      fadeAnimation: false,
      zoomAnimation: false,
      markerZoomAnimation: false,
    }).setView([59.858858145759825, 17.638254092361564], 10);

    document.getElementById("map-task3").classList.remove("leaflet-fade-anim");
    document.getElementById("l1").style.display = "none";

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(
      task3Map
    );

    fetch("../static/js/supermarket.geojson")
      .then((response) => response.json())
      .then((data) => {
        const buffers = data.features.map((feature) => {
          const coords = feature.geometry.coordinates;
          const buffer = turf.buffer(feature, 1, { units: "kilometers" });
          return { feature, buffer, intersects: false };
        });

        for (let i = 0; i < buffers.length; i++) {
          for (let j = 0; j < buffers.length; j++) {
            if (
              i !== j &&
              turf.booleanIntersects(buffers[i].buffer, buffers[j].buffer)
            ) {
              buffers[i].intersects = true;
              break;
            }
          }
        }

        const isolated = buffers.filter((b) => !b.intersects);
        isolated.forEach((b) => {
          const coords = b.feature.geometry.coordinates;
          const latlng = [coords[1], coords[0]];
          L.circle(latlng, {
            radius: 1000,
            color: "blue",
            dashArray: "5.5",
            fillOpacity: 0.1,
            weight: 2,
          })
            .bindPopup(`<b>${b.feature.properties.name}</b>`)
            .addTo(task3Map);
        });

        const overlapping = buffers.filter((b) => b.intersects);
        overlapping.forEach((b) => {
          const coords = b.feature.geometry.coordinates;
          const latlng = [coords[1], coords[0]];
          L.circle(latlng, {
            radius: 1000,
            color: "red",
            dashArray: "1",
            fillOpacity: 0.05,
            weight: 2,
          })
            .bindPopup(`<b>${b.feature.properties.name}</b>`)
            .addTo(task3Map);
        });

        data.features.forEach((feature) => {
          const coords = feature.geometry.coordinates;
          const latlng = [coords[1], coords[0]];
          L.marker(latlng)
            .bindPopup(`<b>${feature.properties.name}</b>`)
            .addTo(task3Map);
        });
      });
  }, 100);
}

function clearTask3() {
  if (task3Map) {
    task3Map.remove();
    document.getElementById("map-task3").style.display = "none";
    task3Map = null;
    document.getElementById("l1").style.display = "none";
  }
}
