// skalat_detail.js
document.addEventListener('DOMContentLoaded', function() {
    // O'chirish tugmasi uchun confirm
    const deleteBtn = document.querySelector('.btn-delete');
    if (deleteBtn) {
        deleteBtn.addEventListener('click', function(e) {
            if (!confirm('Haqiqatan ham ushbu omborni (skalat) o‘chirmoqchimisiz? Undagi barcha mahsulotlar omborsiz qoladi.')) {
                e.preventDefault();
            }
        });
    }
});