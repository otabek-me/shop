// create_skalat.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('#create-skalat-form');
    const submitBtn = document.querySelector('.btn-submit');

    if (form && submitBtn) {
        form.addEventListener('submit', function() {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="loading-spinner"></span> Saqlanmoqda...';
        });
    }

    // Nomi maydoniga avto-fokus
    const nameInput = document.getElementById('id_name');
    if (nameInput) {
        nameInput.focus();

        // Real-time validatsiya
        nameInput.addEventListener('input', function() {
            const val = this.value.trim();
            if (val.length === 0) {
                this.setCustomValidity('Ombor nomi bo‘sh bo‘lishi mumkin emas');
            } else if (val.length < 2) {
                this.setCustomValidity('Ombor nomi kamida 2 harfdan iborat bo‘lishi kerak');
            } else if (val.length > 50) {
                this.setCustomValidity('Ombor nomi 50 ta belgidan oshmasligi kerak');
            } else {
                this.setCustomValidity('');
            }
        });
    }
});