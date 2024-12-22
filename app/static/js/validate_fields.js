const form = document.querySelector(".js-validation-fields");
const emailInput = form.querySelector('input[name="email"]');
const fullNameInput = form.querySelector('input[name="fullName"]');
const passwordInput = form.querySelector('input[name="password"]');

function isEmail(email) {
    return /\S+@\S+\.\S+/.test(email);
}

function isValidFullName(fullName) {
    fullName = fullName.trim();
    const parts = fullName.split(' ');
    return parts.length >= 2;
}

function isValidPassword(password) {
    return password.length >= 5;
}

function markValidation(element, condition) {
    !condition ? element.classList.add('no-valid') : element.classList.remove('no-valid');
}

function validateEmail() {
    setTimeout(function () {
            markValidation(emailInput, isEmail(emailInput.value));
        },
        1000
    );
}

function validateFullName() {
    setTimeout(function () {
            markValidation(fullNameInput, isValidFullName(fullNameInput.value));
        },
        1000
    );
}

function validatePassword() {
    setTimeout(function () {
            markValidation(passwordInput, isValidPassword(passwordInput.value));
        },
        1000
    );
}

emailInput.addEventListener('keyup', validateEmail);
fullNameInput.addEventListener('keyup', validateFullName);
passwordInput.addEventListener('keyup', validatePassword);