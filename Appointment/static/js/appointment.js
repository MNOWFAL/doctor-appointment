// Get the date input and button elements
const dateInput = document.getElementById('date-input');
const appointmentBtn = document.getElementById('appointment-btn');
const viewAppointmentsBtn = document.getElementById('view-appointments-btn');

// Add an event listener to the date input
dateInput.addEventListener('input', () => {
  // Check if a date is selected
  if (dateInput.value!== '') {
    // Enable the appointment button
    appointmentBtn.href = "{% url 'patient:list' %}";
    appointmentBtn.disabled = false;
    viewAppointmentsBtn.href = "{% url 'patient:list' %}";
    viewAppointmentsBtn.disabled = false;
  } else {
    // Disable the appointment button
    appointmentBtn.href = '#';
    appointmentBtn.disabled = true;
    viewAppointmentsBtn.href = '#';
    viewAppointmentsBtn.disabled = true;
  }
});