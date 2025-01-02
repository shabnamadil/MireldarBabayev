const REGISTER_URL = `${location.origin}/api/register/`;
const registerForm = document.getElementById('registerForm');
const successRegisterMessage = document.getElementById('successRegisterMessage');


async function register() {
    const formData = new FormData(registerForm);
    const csrfToken = document.querySelector('input[name="csrfmiddlewaretoken"]').value;

    try {
        const response = await fetch(REGISTER_URL, {
            method: 'POST',
            headers: {
                'X-CSRFToken': csrfToken
            },
            body: formData
        });
        
        if (response.ok) {
            registerForm.reset();
            successRegisterMessage.classList.remove('d-none');
    
            setTimeout(() => {
                window.location.href = `${location.origin}/login`;
            }, 2000);

        } else {
            const errorData = await response.json();
            displayRegisterErrors(errorData);
        }
    } catch (error) {
        console.error('An error occurred:', error);
    }
}

registerForm.addEventListener('submit', function(e) {
    e.preventDefault();
    register();
});

function displayRegisterErrors(errors) {

    // Loop through each field and its corresponding error messages
    for (const [fieldName, messages] of Object.entries(errors)) {
        const translatedMessages = Array.isArray(messages) 
            ? messages.map(translateMessage).join('<br>')
            : translateMessage(messages);

        // Create a custom error message container
        const errorContainer = document.getElementById(`${fieldName}_error`);
        if (errorContainer) {
            // Display the error message under the respective input field
            errorContainer.innerHTML = translatedMessages;
            errorContainer.classList.remove('d-none');  // Make error message visible

            // Add an error class to the input field
            const field = document.querySelector(`[name="${fieldName}"]`);
            if (field) {
                field.classList.add('error-border');
                field.addEventListener('input', () => {
                    field.classList.remove('error-border');
                    errorContainer.classList.add('d-none');  // Hide the error when the user starts typing
                });
            }
        }
    }

    // Hide alert message after a timeout (in case it's still visible from previous errors)
    setTimeout(() => {
        Object.values(errors).forEach((messages, idx) => {
            const fieldName = Object.keys(errors)[idx];
            const errorContainer = document.getElementById(`${fieldName}_error`);
            if (errorContainer) {
                errorContainer.classList.add('d-none');
            }
        });
    }, 10000); // 10 seconds
}

function translateMessage(message) {
    const translations = {
        "This field may not be blank.": "Bu sahə tələb edilir.",
    };
    return translations[message] || message;
}