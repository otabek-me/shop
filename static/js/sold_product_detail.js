// sold_product_detail.js
document.addEventListener('DOMContentLoaded', function() {
    // Yetkazish tugmasi uchun confirm (ixtiyoriy)
    const deliverBtn = document.querySelector('.btn-deliver');
    if (deliverBtn) {
        deliverBtn.addEventListener('click', function(e) {
            if (!confirm('Buyurtmani yetkazilgan deb belgilaysizmi?')) {
                e.preventDefault();
            }
        });
    }
});