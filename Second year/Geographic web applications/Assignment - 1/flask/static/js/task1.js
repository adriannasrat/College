let task1Map = null;

function initTask1() {
  const container = document.getElementById("map-task1");
  container.style.display = "block";
  container.offsetHeight;

  setTimeout(() => {
    task1Map = L.map("map-task1").setView(
      [60.48473406314983, 15.430194738712373],
      16,
      {
        fadeAnimation: false,
        zoomAnimation: false,
        markerZoomAnimation: false,
      }
    );

    document.getElementById("map-task1").classList.remove("leaflet-fade-anim");
    document.getElementById("l1").style.display = "none";

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(
      task1Map
    );

    const icon = L.icon({
      iconUrl: "../static/css/images/marker-icon-2x.png",
      iconSize: [25, 41],
      iconAnchor: [12, 41],
      popupAnchor: [1, -34],
      shadowUrl: "../static/css/images/marker-shadow.png",
      shadowSize: [41, 41],
    });

    var latlngs = [
      [60.48598280804984, 15.430119786725555],
      [60.48536697611823, 15.432298319855448],
      [60.4851703333548, 15.43286255272048],
      [60.48446162067913, 15.434337559002472],
      [60.48413605919552, 15.434985515975228],
      [60.48410859731567, 15.43511843805689],
      [60.48365989662844, 15.435852226420508],
      [60.482798508523786, 15.437677262164328],
      [60.48259978662887, 15.438084893417766],
      [60.48219839936672, 15.438963894279055],
      [60.4816454038031, 15.440036213521893],
      [60.4814932948434, 15.440312784412953],
      [60.480405423388675, 15.44197977174261],
    ];

    var polyline = L.polyline(latlngs, { color: "red" })
      .addTo(task1Map)
      .bindPopup(
        "<h3>Stationsgatan</h3><img src= '../static/images/stationsgatan.jpg' width='150px'>"
      );

    var polygonLatLngs = [
      [60.484936391414635, 15.431665798197116],
      [60.48525191584355, 15.432115485484246],
      [60.485784496214734, 15.430566562608647],
      [60.48547345243841, 15.430130502210716],
      [60.484936391414635, 15.431665798197116],
    ];

    var polygon = L.polygon(polygonLatLngs, { color: "blue" })
      .addTo(task1Map)
      .bindPopup(
        "<h3>Högskolan Dalarna</h3><img src= '../static/images/högskolan_dalarna.png' width='150px'>"
      );

    const marker = L.marker([60.4829, 15.4265], { icon }).bindPopup(
      "<h3>Borlänge centralstation</h3><img src= '../static/images/borlänge_cantralstation.jpeg' width='150px'>"
    );
    marker.addTo(task1Map);
  }, 100);
}

function clearTask1() {
  if (task1Map) {
    task1Map.remove();
    document.getElementById("map-task1").style.display = "none";
    task1Map = null;
    document.getElementById("l1").style.display = "none";
  }
}
