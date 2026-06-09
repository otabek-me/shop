// sell_product.js
document.addEventListener('DOMContentLoaded', function() {
    // Select2 ni ishga tushirish (jQuery kerak)
    if (typeof $ !== 'undefined' && $.fn.select2) {
        $('.select2-product').select2({
            placeholder: "Mahsulot nomini yozing...",
            allowClear: true,
            width: '100%'
        });
    }

    const form = document.querySelector('#sell-form');
    const submitBtn = document.querySelector('.btn-submit');
    const productSelect = document.querySelector('#id_product');
    const quantityInput = document.querySelector('#id_quantity');
    const priceInput = document.querySelector('#id_price');
    const totalSpan = document.querySelector('#total-price-value');
    const stockInfoSpan = document.querySelector('#stock-info');
    const productPriceHintSpan = document.querySelector('#product-price-hint');

    // Mahsulot ma'lumotlari (Django'dan JSON sifatida o'tkaziladi)
    let productsData = {};
    if (window.productStockData) {
        productsData = window.productStockData;
    }

    function updateProductInfo() {
        const selectedOption = productSelect?.options[productSelect.selectedIndex];
        const productId = productSelect?.value;
        if (productId && productsData[productId]) {
            const data = productsData[productId];
            if (stockInfoSpan) stockInfoSpan.textContent = data.stock + ' ta';
            if (productPriceHintSpan) productPriceHintSpan.textContent = (data.price || data.tannarx) + ' so\'m';
            // Miqdorni cheklash
            if (quantityInput) {
                quantityInput.max = data.stock;
                if (parseInt(quantityInput.value) > data.stock) {
                    quantityInput.value = data.stock;
                }
            }
            // Agar narx maydoni bo'sh bo'lsa, tavsiya etilgan narxni qo'yish
            if (priceInput && !priceInput.value && data.price) {
                priceInput.value = data.price;
            }
        } else {
            if (stockInfoSpan) stockInfoSpan.textContent = '—';
            if (productPriceHintSpan) productPriceHintSpan.textContent = '—';
            if (quantityInput) quantityInput.max = '';
        }
        calculateTotal();
    }

    function calculateTotal() {
        const quantity = parseInt(quantityInput?.value) || 0;
        const price = parseInt(priceInput?.value) || 0;
        const total = quantity * price;
        if (totalSpan) totalSpan.textContent = total.toLocaleString() + ' so\'m';
    }

    function validateQuantity() {
        const selectedOption = productSelect?.options[productSelect.selectedIndex];
        const productId = productSelect?.value;
        if (productId && productsData[productId]) {
            const maxStock = productsData[productId].stock;
            const quantity = parseInt(quantityInput?.value) || 0;
            if (quantity > maxStock) {
                quantityInput.setCustomValidity(`Maksimal ${maxStock} ta sotish mumkin`);
                return false;
            } else {
                quantityInput.setCustomValidity('');
            }
        }
        return true;
    }

    if (productSelect) {
        productSelect.addEventListener('change', updateProductInfo);
    }
    if (quantityInput) {
        quantityInput.addEventListener('input', function() {
            validateQuantity();
            calculateTotal();
        });
    }
    if (priceInput) {
        priceInput.addEventListener('input', calculateTotal);
    }

    // Form submit loading va validatsiya
    if (form && submitBtn) {
        form.addEventListener('submit', function(e) {
            if (!validateQuantity()) {
                e.preventDefault();
                return;
            }
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="loading-spinner"></span> Sotilmoqda...';
        });
    }

    // Boshlang'ich ma'lumotni yangilash
    updateProductInfo();
});