function setupLogoutButton() {
    const logoutButton = document.getElementById('logoutButton');
    if (logoutButton) {
        logoutButton.addEventListener('click', async function (e) {
            e.preventDefault();
            await logoutUser();
        });
    }
}

async function logoutUser() {
    const LOGOUT_URL = `${location.origin}/${lang}/api/logout/`;
    try {
        const response = await authFetch(LOGOUT_URL, {
            method: 'POST'
        });
        if (response.ok) {
            window.location.href = '/login';
        }
    } catch (error) {
        console.error('Error logout user:', error);
    }
}