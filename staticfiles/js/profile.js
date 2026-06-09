// profile.js
document.addEventListener('DOMContentLoaded', function() {
    // Nusxa ko‘chirish funksiyasi
    const copyButtons = document.querySelectorAll('.copy-btn');
    copyButtons.forEach(btn => {
        btn.addEventListener('click', function() {
            const targetId = this.getAttribute('data-copy');
            const targetElement = document.getElementById(targetId);
            if (targetElement) {
                const text = targetElement.innerText.trim();
                navigator.clipboard.writeText(text).then(() => {
                    // Qisqa vaqt ichida tugma matnini o‘zgartirish
                    const originalHtml = this.innerHTML;
                    this.innerHTML = '<i class="fas fa-check"></i>';
                    setTimeout(() => {
                        this.innerHTML = originalHtml;
                    }, 1500);
                }).catch(err => {
                    console.error('Nusxa olishda xatolik:', err);
                });
            }
        });
    });
});