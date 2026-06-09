// product_list.js
document.addEventListener('DOMContentLoaded', function() {
    // DOM elementlari
    const searchInput = document.getElementById('searchInput');
    const categoryFilter = document.getElementById('categoryFilter');
    const stockFilterBtns = document.querySelectorAll('.stock-filter-btn');
    const productRows = document.querySelectorAll('.product-row');
    let currentStockFilter = 'all';

    // Filtrlash funksiyasi
    function filterProducts() {
        const searchTerm = searchInput ? searchInput.value.toLowerCase() : '';
        const selectedCategory = categoryFilter ? categoryFilter.value : '';

        productRows.forEach(row => {
            const name = row.getAttribute('data-name')?.toLowerCase() || '';
            const category = row.getAttribute('data-category') || '';
            const stock = parseInt(row.getAttribute('data-stock') || '0');

            let matchesSearch = name.includes(searchTerm);
            let matchesCategory = selectedCategory === '' || category === selectedCategory;
            let matchesStock = true;

            if (currentStockFilter === 'low') {
                matchesStock = stock > 0 && stock <= 3;
            } else if (currentStockFilter === 'out') {
                matchesStock = stock === 0;
            } else if (currentStockFilter === 'in') {
                matchesStock = stock > 0;
            }

            if (matchesSearch && matchesCategory && matchesStock) {
                row.style.display = '';
            } else {
                row.style.display = 'none';
            }
        });

        // Bo'sh holatni ko'rsatish
        const visibleRows = document.querySelectorAll('.product-row[style="display: none;"]');
        const anyVisible = document.querySelectorAll('.product-row:not([style*="display: none"])').length > 0;
        const emptyMsg = document.getElementById('emptyMessage');
        if (emptyMsg) {
            emptyMsg.style.display = anyVisible ? 'none' : 'block';
        }
    }

    // Qidirish hodisasi
    if (searchInput) {
        searchInput.addEventListener('input', filterProducts);
    }

    // Kategoriya filtri
    if (categoryFilter) {
        categoryFilter.addEventListener('change', filterProducts);
    }

    // Stok filtri tugmalari
    stockFilterBtns.forEach(btn => {
        btn.addEventListener('click', function() {
            stockFilterBtns.forEach(b => b.classList.remove('active'));
            this.classList.add('active');
            currentStockFilter = this.getAttribute('data-filter');
            filterProducts();
        });
    });

    // O'chirish confirm
    const deleteBtns = document.querySelectorAll('.delete-btn');
    deleteBtns.forEach(btn => {
        btn.addEventListener('click', function(e) {
            if (!confirm('Haqiqatan ham ushbu mahsulotni o‘chirmoqchimisiz?')) {
                e.preventDefault();
            }
        });
    });
});