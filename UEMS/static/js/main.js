document.addEventListener("DOMContentLoaded", function () {
    const buttons = document.querySelectorAll(".event-card button");

    buttons.forEach(button => {
        button.addEventListener("click", function (event) {
            event.stopPropagation(); // Prevents triggering the card link
            event.preventDefault(); // Prevents navigation

            let confirmRegistration = confirm("Are you sure you want to register for this event?");

            if (confirmRegistration) {
                // Show a success message (without backend)
                alert("✅ Registration successful!");
            }
        });
    });
});
