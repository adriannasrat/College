let task4Map = null;

function initTask4() {
  const container = document.getElementById("map-task4");
  container.style.display = "block";
  container.offsetHeight;

  setTimeout(() => {
    task4Map = L.map("map-task4").setView([59.609, 16.454], 16, {
      fadeAnimation: false,
      zoomAnimation: false,
      markerZoomAnimation: false,
    });

    document.getElementById("l1").style.display = "none";
    document.getElementById("map-task1").classList.remove("leaflet-fade-anim");

    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png").addTo(
      task4Map
    );

    const imageUrl = "../static/images/ikea_vasteras.png";
    const imageBounds = [
      [59.61041263146507, 16.451161483320362],
      [59.61017382187154, 16.450453380140175],
      [59.60996214831289, 16.450163701566282],
      [59.60832841778222, 16.455453017744134],
      [59.6082415727397, 16.45537791589186],
      [59.60817101097777, 16.45557103494059],
      [59.607438245459434, 16.454701999219765],
      [59.60684659349303, 16.456482986005483],
      [59.607183130751025, 16.456879952939772],
      [59.60713427877758, 16.45698724130017],
      [59.60805159842727, 16.458070853742527],
      [59.60810044906765, 16.457909921201974],
      [59.6084586849245, 16.458360532316476],
      [59.610081554074185, 16.45322141984397],
      [59.60994586567628, 16.452996114286293],
      [59.61027694440446, 16.45200906136907],
      [59.61019553190471, 16.451848128827663],
      [59.61041263146507, 16.451161483320362],
    ];
    L.imageOverlay(imageUrl, imageBounds).addTo(task4Map);
  }, 100);
}

function clearTask4() {
  if (task4Map) {
    task4Map.remove();
    document.getElementById("map-task4").style.display = "none";
    task4Map = null;
  }
}
