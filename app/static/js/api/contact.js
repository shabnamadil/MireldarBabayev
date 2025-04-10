const CONTACT_URL = `${location.origin}/api/contact/`;
const contactForm = document.getElementById('contactPostForm');
const successContactMessage = document.getElementById('successContactMessage');
const alertContactMessage = document.getElementById('alertContactMessage');

async function contact() {
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const formData = new FormData(contactForm);

    try {
        const response = await fetch(CONTACT_URL, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        });

        if (response.ok) {
            contactForm.reset();
            displayContactSuccessMessage();
        } else {
            const errorData = await response.json();
            displayContactErrors(errorData);
        }
    } catch (error) {
        console.error('An error occurred:', error);
        displayContactErrors({ error: 'An unexpected error occurred. Please try again.' });
    }
}

contactForm.addEventListener('submit', function(e) {
    e.preventDefault();
    contact();
});

function displayContactErrors(errors) {
    alertContactMessage.classList.remove('d-none');
    let errorContent = '';

    for (const [fieldName, messages] of Object.entries(errors)) {
        const translatedMessages = Array.isArray(messages) 
            ? messages.map(translateContactMessage).join('<br>')
            : translateContactMessage(messages);
        
        errorContent += `${translatedMessages}<br>`;
        
        const field = document.querySelector(`[name="${fieldName}"]`);
        if (field) {
            field.classList.add('error-border');
            field.addEventListener('input', () => {
                field.classList.remove('error-border');
            });
        }
    }

    alertContactMessage.innerHTML = errorContent;

    setTimeout(() => {
        alertContactMessage.classList.add('d-none');
    }, 10000); // 10 seconds
}

function displayContactSuccessMessage() {
    successContactMessage.classList.remove('d-none');

    setTimeout(() => {
        successContactMessage.classList.add('d-none');
    }, 10000); // 10 seconds
}

function translateContactMessage(message) {
    const translations = {
        "This field may not be blank.": "Bu sahə tələb edilir.",
    };
    return translations[message] || message;
}
