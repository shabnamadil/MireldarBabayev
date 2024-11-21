const APPOINTMENT_URL = `${location.origin}/api/appointment/`;
const appointmentForm = document.getElementById('appointmentPostForm');
const successMessage = document.getElementById('successMessage');
const alertMessage = document.getElementById('alertMessage');

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
            displaySuccessMessage();
        } else {
            const errorData = await response.json();
            displayErrors(errorData);
        }
    } catch (error) {
        console.error('An error occurred:', error);
        displayErrors({ error: 'An unexpected error occurred. Please try again.' });
    }
}

appointmentForm.addEventListener('submit', function(e) {
    e.preventDefault();
    appointment();
});

function displayErrors(errors) {
    alertMessage.classList.remove('d-none');
    let errorContent = '';

    for (const [fieldName, messages] of Object.entries(errors)) {
        const translatedMessages = Array.isArray(messages) 
            ? messages.map(translateMessage).join('<br>')
            : translateMessage(messages);
        
        errorContent += `${translatedMessages}<br>`;
        
        const field = document.querySelector(`[name="${fieldName}"]`);
        if (field) {
            field.classList.add('error-border');
            field.addEventListener('input', () => {
                field.classList.remove('error-border');
            });
        }
    }

    alertMessage.innerHTML = errorContent;

    setTimeout(() => {
        alertMessage.classList.add('d-none');
    }, 10000); // 10 seconds
}

function displaySuccessMessage() {
    successMessage.classList.remove('d-none');

    setTimeout(() => {
        successMessage.classList.add('d-none');
    }, 10000); // 10 seconds
}

function translateMessage(message) {
    const translations = {
        "This field may not be blank.": "Bu sahə tələb edilir.",
    };
    return translations[message] || message;
}
