let task2Map = null;

function initTask2() {
  const container = document.getElementById("map-task2");
  container.style.display = "block";
  container.offsetHeight;

  if (L.DomUtil.get("map-task2")._leaflet_id) {
    L.DomUtil.get("map-task2")._leaflet_id = null;
  }

  setTimeout(() => {
    document.getElementById("l1").style.display = "inline-block";
    task2Map = L.map("map-task2").setView([60.488, 15.421], 15, {
      fadeAnimation: false,
      zoomAnimation: false,
      markerZoomAnimation: false,
    });

    document.getElementById("map-task2").classList.remove("leaflet-fade-anim");

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(
      task2Map
    );

    document.getElementById("sidebar").style.display = "block"; // ✅ Ensure it's visible
    const sidebar = L.control.sidebar("sidebar", { position: "left" });
    task2Map.addControl(sidebar);
    document.getElementById("l1").addEventListener("click", function () {
      if (sidebar.isVisible()) {
        sidebar.hide();
        this.innerText = "Show sidebar";
      } else {
        sidebar.show();
        this.innerText = "Hide sidebar";
      }
    });

    const polylineMeasure = L.control.polylineMeasure({
      position: "topleft",
      unit: "metres",
      showBearings: false,
      clearMeasurementsOnStop: false,
      showClearControl: false,
      showUnitControl: false,
      measureControlLabel: "",
      backgroundColor: "transparent",
    });
    polylineMeasure.addTo(task2Map);

    locations.forEach(function (loc) {
      var marker = L.marker([loc.lat, loc.lng]).addTo(task2Map);
      marker.on("click", function () {
        document.getElementById("sidebar").innerHTML =
          "<h2>" +
          loc.name +
          "</h2>" +
          "<p><b>Koordinater:</b> " +
          loc.lat +
          ", " +
          loc.lng +
          "</p>" +
          "<p>" +
          loc.info +
          "</p>";
      });
    });

    const line1coords = [
      { lat: 60.487207, lng: 15.433974 },
      { lat: 60.484232, lng: 15.417956 },
      { lat: 60.491811, lng: 15.410227 },
      { lat: 60.488086, lng: 15.430546 },
      { lat: 60.492604, lng: 15.416041 },
    ];
    polylineMeasure.seed([line1coords]);
  }, 100);
}

function clearTask2() {
  function clearTask2() {
    if (task2Map) {
      task2Map.remove();
      document.getElementById("map-task2").style.display = "none";
      task2Map = null;
    }

    const sidebarEl = document.getElementById("sidebar");
    document.getElementById("l1").style.display = "none";
    if (sidebarEl) {
      sidebarEl.style.display = "none"; // ✅ Safe access
    }
  }
}
