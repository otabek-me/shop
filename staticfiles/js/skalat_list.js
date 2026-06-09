// skalat_list.js
document.addEventListener('DOMContentLoaded', function() {
    // Qidirish funksiyasi
    const searchInput = document.getElementById('searchInput');
    const tableRows = document.querySelectorAll('.skalat-row');

    function filterSkalats() {
        const searchTerm = searchInput.value.toLowerCase();
        tableRows.forEach(row => {
            const name = row.getAttribute('data-name')?.toLowerCase() || '';
            if (name.includes(searchTerm)) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });
        // Bo'sh holatni ko'rsatish (ixtiyoriy)
        const visibleRows = document.querySelectorAll('.skalat-row[style="display: none;"]');
        const anyVisible = document.querySelectorAll('.skalat-row:not([style*="display: none"])').length > 0;
        const emptyMsg = document.getElementById('emptyMessage');
        if (emptyMsg) {
            emptyMsg.style.display = anyVisible ? 'none' : 'block';
        }
    }

    if (searchInput) {
        searchInput.addEventListener('input', filterSkalats);
    }

    // O'chirish confirm
    const deleteBtns = document.querySelectorAll('.delete-btn');
    deleteBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            if (!confirm('Haqiqatan ham ushbu omborni (skalat) o‘chirmoqchimisiz? Undagi barcha mahsulotlar omborsiz qoladi.')) {
                e.preventDefault();
            }
        });
    });
});