Title: Rantevou
Slug: appointment
Status: draft

 <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/css/bootstrap.min.css">
    <script src="https://cdnjs.cloudflare.com/ajax/libs/jquery/3.6.4/jquery.min.js"></script>
    <script src="https://cdnjs.cloudflare.com/ajax/libs/bootstrap/5.3.0/js/bootstrap.bundle.min.js"></script>

<div class="container mt-5">
        <h1 class="text-center">Book an Appointment</h1>
        <form id="appointment-form" class="mt-4">
            <div class="mb-3">
                <label for="appointment-date" class="form-label">Select Date</label>
                <input type="date" id="appointment-date" class="form-control" required>
            </div>
            <div class="mb-3">
                <label for="appointment-time" class="form-label">Select Time</label>
                <select id="appointment-time" class="form-select" required>
                    <option value="">-- Select a Time Slot --</option>
                </select>
            </div>
            <button type="submit" class="btn btn-primary">Book Appointment</button>
        </form>
        <div id="success-message" class="alert alert-success mt-3" style="display: none;">
            Appointment booked successfully!
        </div>
        <div id="error-message" class="alert alert-danger mt-3" style="display: none;">
            Failed to book appointment. Please try again.
        </div>
    </div>
    <script>
        $(document).ready(function () {
            const unavailableSlots = {};

            // Fetch unavailable slots from the server (to be implemented in Python backend)
            function fetchUnavailableSlots(date) {
                $.get(`/api/unavailable-slots?date=${date}`, function (data) {
                    unavailableSlots[date] = data;
                    updateTimeSlots(date);
                }).fail(function () {
                    console.error("Failed to fetch unavailable slots");
                });
            }

            // Update time slots based on unavailable slots
            function updateTimeSlots(date) {
                const timeSelect = $("#appointment-time");
                timeSelect.empty();
                const allSlots = ["09:00", "10:00", "11:00", "12:00", "14:00", "15:00", "16:00"];

                allSlots.forEach(slot => {
                    const isUnavailable = unavailableSlots[date]?.includes(slot);
                    const option = $(`<option value="${slot}">${slot}</option>`);
                    if (isUnavailable) option.addClass("inactive").prop("disabled", true);
                    timeSelect.append(option);
                });
            }

            // Handle date selection
            $("#appointment-date").on("change", function () {
                const selectedDate = $(this).val();
                if (selectedDate) fetchUnavailableSlots(selectedDate);
            });

            // Handle form submission
            $("#appointment-form").on("submit", function (e) {
                e.preventDefault();

                const date = $("#appointment-date").val();
                const time = $("#appointment-time").val();

                if (!date || !time) return alert("Please select a valid date and time.");

                $.post("/api/book-appointment", { date, time }, function () {
                    $("#success-message").show();
                    $("#error-message").hide();
                }).fail(function () {
                    $("#success-message").hide();
                    $("#error-message").show();
                });
            });
        });
    </script>