document.addEventListener("DOMContentLoaded", function addMessage() {
    if (document.getElementById("popup")) {
        const message = document.getElementsByClassName("message-data");
        const popup = document.getElementById("popup");
        const popupContent = document.getElementById("popup-content");
        const popupClose = document.getElementById("popup-close");
        const overlay = document.getElementById("overlay");
        console.log(message[0].textContent);
        popupContent.textContent = message[0].textContent;
        popup.style.display = "block";
        overlay.style.display = "block";

        popupClose.addEventListener("click", function() {
            popup.style.display = "none";
            overlay.style.display = "none";
        });

        overlay.addEventListener("click", function() {
            popup.style.display = "none";
            overlay.style.display = "none";
        });
    };
});

async function submitForm(event) {
    event.preventDefault();
    console.log(event);
    const formData = new FormData(event.target);
    const popup = document.getElementById("popup");
    const popupContent = document.getElementById("popup-content");
    const popupClose = document.getElementById("popup-close");
    const overlay = document.getElementById("overlay");
    const csrfToken = document.querySelector('[name=csrfmiddlewaretoken]').value;
    
    try {
        const response = await fetch(url, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken,
            },
            body: formData,
        });
        const data = await response.json();
        if (data.status === 'success') {
            var result = data.message;
        } else {
            var result = 'Form submission failed. Errors: ' + JSON.stringify(data.errors);
        }
        popupContent.textContent = result;
        popup.style.display = "block";
        overlay.style.display = "block";

    } catch (error) {
        console.error('Error:', error);
    }
    popupClose.addEventListener("click", function() {
        popup.style.display = "none";
        overlay.style.display = "none";
    });

    overlay.addEventListener("click", function() {
    popup.style.display = "none";
    overlay.style.display = "none";
    });
};