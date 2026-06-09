// signup.js
document.addEventListener('DOMContentLoaded', function() {
    // Parolni ko'rsatish/yashirish
    const toggleButtons = document.querySelectorAll('.toggle-password');
    toggleButtons.forEach(button => {
        button.addEventListener('click', function() {
            const targetId = this.getAttribute('data-target');
            const input = document.getElementById(targetId);
            if (input) {
                const type = input.getAttribute('type') === 'password' ? 'text' : 'password';
                input.setAttribute('type', type);
                const icon = this.querySelector('i');
                if (icon) {
                    icon.classList.toggle('fa-eye-slash');
                    icon.classList.toggle('fa-eye');
                }
            }
        });
    });

    // Parol kuchlilik metr
    const passwordInput = document.getElementById('id_password1');
    const strengthBar = document.getElementById('strength-bar');
    const strengthText = document.getElementById('strength-text');

    if (passwordInput && strengthBar && strengthText) {
        passwordInput.addEventListener('input', function() {
            const val = this.value;
            let strength = 0;
            if (val.length >= 6) strength++;
            if (val.length >= 10) strength++;
            if (/[A-Z]/.test(val)) strength++;
            if (/[0-9]/.test(val)) strength++;
            if (/[^A-Za-z0-9]/.test(val)) strength++;

            const percent = (strength / 5) * 100;
            strengthBar.style.width = percent + '%';
            if (percent < 20) {
                strengthBar.style.backgroundColor = '#ef4444';
                strengthText.textContent = 'Juda kuchsiz';
            } else if (percent < 40) {
                strengthBar.style.backgroundColor = '#f59e0b';
                strengthText.textContent = 'Kuchsiz';
            } else if (percent < 60) {
                strengthBar.style.backgroundColor = '#eab308';
                strengthText.textContent = 'O‘rtacha';
            } else if (percent < 80) {
                strengthBar.style.backgroundColor = '#10b981';
                strengthText.textContent = 'Kuchli';
            } else {
                strengthBar.style.backgroundColor = '#059669';
                strengthText.textContent = 'Juda kuchli';
            }
        });
    }

    // Parollar mosligini tekshirish (real-time)
    const password2 = document.getElementById('id_password2');
    if (password2 && passwordInput) {
        function checkMatch() {
            if (password2.value !== passwordInput.value) {
                password2.setCustomValidity('Parollar mos kelmadi');
            } else {
                password2.setCustomValidity('');
            }
        }
        passwordInput.addEventListener('input', checkMatch);
        password2.addEventListener('input', checkMatch);
    }
});