document.addEventListener("DOMContentLoaded", function() {
    // Fetch the form data from the backend when the page is loaded
    fetch('/users/login-register/', {
        method: 'GET', // Send a GET request to fetch form data
    })
    .then(response => response.json())
    .then(data => {
        // Update login and register forms with the received data
        const loginForm = document.getElementById("login-form");
        const registerForm = document.getElementById("register-form");

        if (data.login_form) {
            // Update login form fields based on the received data (e.g., default values)
            loginForm.querySelector('[name="login_username"]').placeholder = data.login_form.login_username || "E-mail";
            loginForm.querySelector('[name="login_password"]').placeholder = data.login_form.login_password || "Password";
        }

        if (data.register_form) {
            // Update register form fields based on the received data (e.g., default values)
            registerForm.querySelector('[name="full_name"]').placeholder = data.register_form.full_name || "Full Name";
            registerForm.querySelector('[name="register_username"]').placeholder = data.register_form.register_username || "E-mail";
            registerForm.querySelector('[name="location"]').placeholder = data.register_form.location || "Location";
            registerForm.querySelector('[name="register_password"]').placeholder = data.register_form.register_password || "Password";
        }
    })
    .catch(error => console.error('Error fetching form data:', error));
});

document.getElementById("login-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    formData.append('action', 'login');  // Append action to distinguish the type

    // Make the POST request via Fetch API (AJAX)
    fetch('/users/login-register/', {
        method: 'POST',
        body: new URLSearchParams(formData)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the backend
        const loginMessages = document.getElementById("login-messages");
        if (data.access_token) {
            loginMessages.innerHTML = "<p>Login successful! Redirecting...</p>";
            window.location.href = '/';  // Redirect to home or dashboard after login
        } else {
            loginMessages.innerHTML = `<ul>${data.errors.map(error => `<li>${error}</li>`).join('')}</ul>`;
        }
    })
    .catch(error => console.error('Error:', error));
});

document.getElementById("register-form").addEventListener("submit", function(event) {
    event.preventDefault();
    const formData = new FormData(this);
    formData.append('action', 'register');  // Append action for registration

    // Make the POST request via Fetch API (AJAX)
    fetch('/users/login-register/', {
        method: 'POST',
        body: new URLSearchParams(formData)
    })
    .then(response => response.json())
    .then(data => {
        // Handle the response from the backend
        const registerMessages = document.getElementById("register-messages");
        if (data.message) {
            registerMessages.innerHTML = "<p>Registration successful! You can now log in.</p>";
        } else {
            registerMessages.innerHTML = `<ul>${data.errors.map(error => `<li>${error}</li>`).join('')}</ul>`;
        }
    })
    .catch(error => console.error('Error:', error));
});
