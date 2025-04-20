let accessToken = null;

function setAccessToken(token) {
    accessToken = token;
}

function getAccessToken() {
    return accessToken;
}

async function refreshAccessToken() {
    try {
        const response = await fetch(`${location.origin}/api/token/refresh/`, {
            method: 'POST',
            credentials: 'include', // ✅ refresh cookie will be sent
        });

        if (!response.ok) {
            const errorResponse = await response.json();
            console.error('Refresh failed:', errorResponse);
            return null;
        }

        const data = await response.json();
        setAccessToken(data.access);
        return data.access;
    } catch (error) {
        console.error('Refresh error:', error);
        return null;
    }
}

async function authFetch(url, options = {}) {
    const token = getAccessToken();

    if (!options.headers) {
        options.headers = {};
    }

    if (token) {
        options.headers['Authorization'] = `Bearer ${token}`;
    }

    let response = await fetch(url, { ...options, credentials: 'include' });

    // If token is expired or invalid, try to refresh
    if (response.status === 401 || response.status === 403) {
        const newToken = await refreshAccessToken();

        if (newToken) {
            options.headers['Authorization'] = `Bearer ${newToken}`;
            response = await fetch(url, { ...options, credentials: 'include' });
        }
    }

    return response;
}