const APPOINTMENT_URL = `${location.origin}/api/appointment/`;
const appointmentForm = document.getElementById('appointmentPostForm');
const successAppointmentMessage = document.getElementById('successAppointmentMessage');
const alertAppointmentMessage = document.getElementById('alertAppointmentMessage');

async function appointment() {
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const formData = new FormData(appointmentForm);

    try {
        const response = await fetch(APPOINTMENT_URL, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        });

        if (response.ok) {
            appointmentForm.reset();
            displayAppointmentSuccessMessage();
        } else {
            const errorData = await response.json();
            displayAppointmentErrors(errorData);
        }
    } catch (error) {
        console.error('An error occurred:', error);
        displayAppointmentErrors({ error: 'An unexpected error occurred. Please try again.' });
    }
}

appointmentForm.addEventListener('submit', function(e) {
    e.preventDefault();
    appointment();
});

function displayAppointmentErrors(errors) {
    alertAppointmentMessage.classList.remove('d-none');
    let errorContent = '';

    for (const [fieldName, messages] of Object.entries(errors)) {
        const translatedMessages = Array.isArray(messages) 
            ? messages.map(translateAppointmentMessage).join('<br>')
            : translateAppointmentMessage(messages);
        
        errorContent += `${translatedMessages}<br>`;
        
        const field = document.querySelector(`[name="${fieldName}"]`);
        if (field) {
            field.classList.add('error-border');
            field.addEventListener('input', () => {
                field.classList.remove('error-border');
            });
        }
    }

    alertAppointmentMessage.innerHTML = errorContent;

    setTimeout(() => {
        alertAppointmentMessage.classList.add('d-none');
    }, 10000); // 10 seconds
}

function displayAppointmentSuccessMessage() {
    successAppointmentMessage.classList.remove('d-none');

    setTimeout(() => {
        successAppointmentMessage.classList.add('d-none');
    }, 10000); // 10 seconds
}

function translateAppointmentMessage(message) {
    const translations = {
        "This field may not be blank.": "Bu sahə tələb edilir.",
    };
    return translations[message] || message;
}
