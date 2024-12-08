const NEWSLETTER_URL = `${location.origin}/api/newsletter/`
const newsletterForm = document.getElementById('newsletterForm')
const newsletterSubmitBtn = document.getElementById('newslettersubmit')
const successSubscribeMessage = document.getElementById('successSubscribeMessage')
const alertSubscribeMessage = document.getElementById('alertSubscribeMessage')

async function newsletter() {
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;
    const formData = new FormData(newsletterForm);

    try {
        const response = await fetch(NEWSLETTER_URL, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        });

        if (response.ok) {
            newsletterForm.reset();
            displayNewsletterSuccessMessage();
        } else {
            const errorData = await response.json();
            console.log(errorData);
            
            displayNewsletterErrors(errorData);
        }
    } catch (error) {
        console.error('An error occurred:', error);
        displayNewsletterErrors({ error: 'An unexpected error occurred. Please try again.' });
    }
}

newsletterSubmitBtn.addEventListener('click', function(e) {
    e.preventDefault();
    newsletter();
});

function displayNewsletterSuccessMessage() {
    successSubscribeMessage.classList.remove('d-none');

    setTimeout(() => {
        successSubscribeMessage.classList.add('d-none');
    }, 10000); // 10 seconds
}

function displayNewsletterErrors(errors) {
    alertSubscribeMessage.classList.remove('d-none');
    let errorContent = '';

    for (const [fieldName, messages] of Object.entries(errors)) {
        const translatedMessages = Array.isArray(messages) 
            ? messages.map(translateSubscribeMessage).join('<br>')
            : translateSubscribeMessage(messages);
        
        errorContent += `${messages}<br>`;
        
        const field = document.querySelector(`[name="${fieldName}"]`);
        if (field) {
            field.classList.add('error-border');
            field.addEventListener('input', () => {
                field.classList.remove('error-border');
            });
        }
    }

    alertSubscribeMessage.innerHTML = errorContent;

    setTimeout(() => {
        alertSubscribeMessage.classList.add('d-none');
    }, 10000); // 10 seconds
}

function translateSubscribeMessage(message) {
    const translations = {
        "This field may not be blank.": "Bu sahə tələb edilir.",
    };
    return translations[message] || message;
}