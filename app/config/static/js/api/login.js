const LOGIN_URL = `${location.origin}/api/token/`;
const loginForm = document.getElementById('loginForm');
const alertLoginMessage = document.getElementById('alertLoginMessage');


// Token-based login
loginForm.addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = new FormData(loginForm)

    try {
        const response = await fetch(LOGIN_URL, {
            method: 'POST',
            body:formData,
        });

        if (response.ok) {
            window.location.href = '/'; // Redirect to the home page
        } else {
            displayLoginErrors();
            return;
        }
    } catch (error) {
        console.error('An error occurred during token-based login:', error);
        return;
    }
});

function displayLoginErrors() {
    alertLoginMessage.classList.remove('d-none');
    let errorContent = gettext('Invalid email or password. Please try again.');
    alertLoginMessage.innerText = errorContent;

    setTimeout(() => {
        alertLoginMessage.classList.add('d-none');
    }, 10000); // Hide error message after 10 seconds
}