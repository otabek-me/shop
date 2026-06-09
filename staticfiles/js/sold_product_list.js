// sold_product_list.js
document.addEventListener('DOMContentLoaded', function() {
    // Checkbox avtomatik yuborish (asl funksiya saqlangan)
    const checkbox = document.getElementById('filter-undelivered');
    if (checkbox) {
        checkbox.addEventListener('change', function() {
            document.getElementById('filter-form').submit();
        });
    }

    // Sana formasi yuborilganda yuklanish belgisi
    const dateForm = document.getElementById('date-form');
    const submitBtn = document.querySelector('.btn-filter');
    if (dateForm && submitBtn) {
        dateForm.addEventListener('submit', function() {
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<i class="fas fa-spinner fa-spin"></i> Filtrlash...';
        });
    }

    // Yetkazish tugmalari uchun confirm (ixtiyoriy)
    const deliverLinks = document.querySelectorAll('.btn-deliver');
    deliverLinks.forEach(link => {
        link.addEventListener('click', function(e) {
            if (!confirm('Buyurtmani yetkazilgan deb belgilaysizmi?')) {
                e.preventDefault();
            }
        });
    });
});