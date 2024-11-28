const LOGIN_URL = `${location.origin}/api/token/`;
const loginForm = document.getElementById('loginForm');
const alertLoginMessage = document.getElementById('alertLoginMessage');

// Handle both session-based login and token-based login in one listener
loginForm.addEventListener('submit', async function(e) {
    e.preventDefault();

    // Token-based login
    const formData = new FormData(loginForm)

    try {
        const response = await fetch(LOGIN_URL, {
            method: 'POST',
            body:formData,
        });

        if (response.ok) {
            const data = await response.json();
            console.log('Token-based login successful:', data);

            // Store the token in a cookie
            setCookie('token', data.access, 1);
        } else {
            displayErrors();
            return;
        }
    } catch (error) {
        console.error('An error occurred during token-based login:', error);
        return;
    }

    // Session-based login (Submit the form)
    this.submit(); // Proceed with normal form submission after token-based login
});

function displayErrors() {
    alertLoginMessage.classList.remove('d-none');
    let errorContent = 'Incorrect email or password';
    alertLoginMessage.innerText = errorContent;

    setTimeout(() => {
        alertLoginMessage.classList.add('d-none');
    }, 10000); // Hide error message after 10 seconds
}

function setCookie(name, value, days) {
    const date = new Date();
    date.setTime(date.getTime() + (days * 24 * 60 * 60 * 1000)); // Set expiration time
    const expires = `expires=${date.toUTCString()}`;
    document.cookie = `${name}=${encodeURIComponent(value)}; ${expires}; path=/`; // Set the cookie
}