// deliver_sold_product.css
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('#deliver-form');
    const submitBtn = document.querySelector('.btn-submit');

    if (form && submitBtn) {
        form.addEventListener('submit', function() {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="loading-spinner"></span> Yetkazilmoqda...';
        });
    }

    // Yetkazib beruvchi tanlash maydoniga fokus
    const deliverField = document.getElementById('id_delievered_by');
    if (deliverField) {
        deliverField.focus();
    }

    // Agar forma allaqachon yetkazilgan bo'lsa, ogohlantirish (oldini olish)
    // Buni Python darajasida ham tekshirish mumkin, lekin frontendda ham yaxshi
    const deliveredFlag = document.querySelector('.delivered-warning');
    if (deliveredFlag) {
        // agar yetkazilgan bo'lsa, tugmani o'chirish
        if (submitBtn) submitBtn.disabled = true;
    }
});