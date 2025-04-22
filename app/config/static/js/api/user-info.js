const USER_INFO = `${location.origin}/api/user/me/`;
const userInfoContainer = document.getElementById('userInfoContainer');


document.addEventListener('DOMContentLoaded', async function () {

    async function displayUserInfo() {
        try {
            const response = await authFetch(USER_INFO);

            if (response.ok) {
                const data = await response.json();
                renderAuthenticatedUserInfo(data);
                setupLogoutButton();
            } else {
                renderGuestUserInfo()
            }


        } catch (error) {
            console.error('Error fetching user info:', error);
        }
    }

    function renderAuthenticatedUserInfo(data) {
        userInfoContainer.innerHTML = ''
        userInfoContainer.innerHTML = `
            <a class="nav-link dropdown-toggle d-flex align-items-center user-nav" href="#" id="userDropdown" role="button"
                data-bs-toggle="dropdown" aria-expanded="false">
                <img src="${data.image}" class="user-img" alt="${data.full_name}}">
            </a>
            <div class="dropdown-menu dropdown-menu-end shadow-lg" aria-labelledby="userDropdown">
                <div id="authenticatedContent">
                    <div class="user-info" id="userInfo">
                        <div class="d-flex align-items-center">
                            <div>
                                <strong>${data.full_name}</strong>
                                <div class="text-muted small">${data.email}</div>
                            </div>
                        </div>
                    </div>
                    <hr class="dropdown-divider">
                    <!-- Links for Logged-In Users -->
                    <a class="dropdown-item text-danger cursor" id="logoutButton">
                        <i class="fas fa-sign-out-alt"></i> ${gettext('Logout')}
                    </a>
                </div>
            </div>
    `

    }

    function renderGuestUserInfo() {
        userInfoContainer.innerHTML = ''
        userInfoContainer.innerHTML = `
        <a class="nav-link dropdown-toggle d-flex align-items-center user-nav" href="#" id="userDropdown" role="button"
        data-bs-toggle="dropdown" aria-expanded="false">
        <img src="${STATIC.userImage}" class="user-img" alt="Mireldar Babayev">
        </a>
        <div class="dropdown-menu dropdown-menu-end shadow-lg" aria-labelledby="userDropdown">
            <div> <!-- Guest Info Section -->
                <div class="guest-info">
                    <strong>${gettext('Welcome, Guest!')}</strong>
                    <p class="text-muted small mb-2">${gettext('Please login or register to access your account.')}</p>
                </div>
                <hr class="dropdown-divider">
                <!-- Links for Guests -->
                <a class="dropdown-item" href="${URLS.login}">
                    <i class="fas fa-sign-in-alt text-secondary"></i> ${gettext('Login')}
                </a>
                <a class="dropdown-item" href="${URLS.register}">
                    <i class="fas fa-user-plus text-secondary"></i> ${gettext('Register')}
                </a>
            </div>
        </div>
    `
    }

    displayUserInfo();

})
