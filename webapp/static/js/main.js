// Get all availible buttons
const addTaskButton = document.getElementById('addTaskButton');
const clearTaskButton = document.getElementById('clearTaskButton');

// When button clicked, do this...
addTaskButton.addEventListener("click", () => {
    // action
    window.location.href = "{% url '/' %}";
});

clearTaskButton.addEventListener("click", () => {
    // action
});


