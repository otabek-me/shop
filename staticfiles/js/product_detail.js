// product_detail.js
document.addEventListener('DOMContentLoaded', function() {
    // O'chirish tugmasi uchun confirm
    const deleteBtn = document.querySelector('.btn-delete');
    if (deleteBtn) {
        deleteBtn.addEventListener('click', function(e) {
            if (!confirm('Haqiqatan ham ushbu mahsulotni o‘chirmoqchimisiz? Bu amalni qaytarib bo‘lmaydi.')) {
                e.preventDefault();
            }
        });
    }

    // Agar soni 3 dan kam bo'lsa, qizil rangda ko'rsatish (CSS da ham bor, lekin dinamik)
    const stockSpan = document.querySelector('.product-stock');
    if (stockSpan) {
        const stockText = stockSpan.innerText;
        const match = stockText.match(/\d+/);
        if (match) {
            const stock = parseInt(match[0]);
            if (stock <= 0) {
                stockSpan.style.background = '#ef4444';
            } else if (stock <= 3) {
                stockSpan.style.background = '#f59e0b';
            }
        }
    }
});