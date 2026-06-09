// profile_update.js
document.addEventListener('DOMContentLoaded', function() {
    // Telefon raqamni formatlash (ixtiyoriy)
    const phoneInput = document.getElementById('id_phone');
    if (phoneInput) {
        phoneInput.addEventListener('input', function(e) {
            let value = e.target.value.replace(/\D/g, '');
            if (value.length > 12) value = value.slice(0, 12);
            if (value.startsWith('998') && value.length > 3) {
                let formatted = '+' + value.slice(0, 3) + ' ' + value.slice(3, 5) + ' ' + value.slice(5, 8) + ' ' + value.slice(8, 10) + ' ' + value.slice(10, 12);
                e.target.value = formatted.trim();
            } else if (value.length > 0) {
                e.target.value = '+' + value;
            }
        });
    }

    // Email validatsiya (simple)
    const emailInput = document.getElementById('id_email');
    if (emailInput) {
        emailInput.addEventListener('blur', function() {
            const email = this.value;
            const regex = /^[^\s@]+@([^\s@.,]+\.)+[^\s@.,]{2,}$/;
            if (email && !regex.test(email)) {
                this.setCustomValidity('Email noto‘g‘ri formatda');
            } else {
                this.setCustomValidity('');
            }
        });
    }
});