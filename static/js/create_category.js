// create_category.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('#create-category-form');
    const submitBtn = document.querySelector('.btn-submit');

    if (form && submitBtn) {
        form.addEventListener('submit', function(e) {
            // Submit tugmasini o‘chirish va loading holatiga o‘tkazish
            const originalText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="loading-spinner"></span> Saqlanmoqda...';

            // Forma yuborilgandan keyin tugma qayta tiklanmaydi (sahifa reload bo‘ladi)
            // Agar xatolik bo‘lsa, bu JavaScript qayta ishlamaydi, shuning uchun muammo yo‘q.
            // Agar xohlasangiz, setTimeout bilan qayta tiklash mumkin, lekin kerak emas.
        });
    }

    // Kategoriya nomi maydoniga avto-fokus
    const nameInput = document.getElementById('id_name');
    if (nameInput) {
        nameInput.focus();

        // Real-time validatsiya: bo'sh bo'lmasligi va uzunligi
        nameInput.addEventListener('input', function() {
            const val = this.value.trim();
            if (val.length === 0) {
                this.setCustomValidity('Kategoriya nomi bo‘sh bo‘lishi mumkin emas');
            } else if (val.length < 2) {
                this.setCustomValidity('Kategoriya nomi kamida 2 harfdan iborat bo‘lishi kerak');
            } else if (val.length > 50) {
                this.setCustomValidity('Kategoriya nomi 50 ta belgidan oshmasligi kerak');
            } else {
                this.setCustomValidity('');
            }
        });
    }
});