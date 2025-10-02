$(document).ready(function () {
  // Track which tasks are currently active
  let taskStatus = {
    task1: false,
    task2: false,
    task3: false,
    task4: false,
    task5: false,
  };

  function hideAllMaps() {
    document.querySelectorAll(".map-container").forEach((div) => {
      div.style.display = "none";
    });
  }

  function toggleTask(taskKey, initFn, clearFn) {
    // If the task is already active, do nothing
    if (taskStatus[taskKey]) return;

    // Hide all maps
    hideAllMaps();

    // Clear all other active tasks
    for (let key in taskStatus) {
      if (taskStatus[key]) {
        const clear = window[`clearTask${key.slice(-1)}`];
        if (typeof clear === "function") clear();
        taskStatus[key] = false;
      }
    }

    // Start the selected task
    setTimeout(() => initFn(), 50);
    taskStatus[taskKey] = true;
  }
  $("#toggle-task1").click(() => toggleTask("task1", initTask1, clearTask1));
  $("#toggle-task2").click(() => toggleTask("task2", initTask2, clearTask2));
  $("#toggle-task3").click(() => toggleTask("task3", initTask3, clearTask3));
  $("#toggle-task4").click(() => toggleTask("task4", initTask4, clearTask4));
  $("#toggle-task5").click(() => toggleTask("task5", initTask5, clearTask5));

  // Automatically show Task 1 on page load
  $("#toggle-task1").trigger("click");
});
