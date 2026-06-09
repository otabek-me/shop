// create_product.js
document.addEventListener('DOMContentLoaded', function() {
    const form = document.querySelector('#create-product-form');
    const submitBtn = document.querySelector('.btn-submit');

    // Submit loading holati
    if (form && submitBtn) {
        form.addEventListener('submit', function() {
            const originalText = submitBtn.innerHTML;
            submitBtn.disabled = true;
            submitBtn.innerHTML = '<span class="loading-spinner"></span> Saqlanmoqda...';
        });
    }

    // Soni maydoni - faqat musbat son
    const sonInput = document.getElementById('id_son');
    if (sonInput) {
        sonInput.addEventListener('input', function() {
            let val = parseInt(this.value);
            if (isNaN(val) || val < 0) {
                this.value = 0;
            }
        });
    }

    // Tannarx va sotish narxi - musbat butun son
    const tannarxInput = document.getElementById('id_tannarx');
    const sotishInput = document.getElementById('id_sotish');

    function validateNumber(input) {
        if (input) {
            input.addEventListener('input', function() {
                let val = parseInt(this.value);
                if (isNaN(val) || val < 0) {
                    this.value = 0;
                }
            });
        }
    }
    validateNumber(tannarxInput);
    validateNumber(sotishInput);

    // Agar sotish narxi tannarxdan past bo'lsa ogohlantirish (ixtiyoriy)
    if (tannarxInput && sotishInput) {
        function checkPrice() {
            const tannarx = parseInt(tannarxInput.value) || 0;
            const sotish = parseInt(sotishInput.value) || 0;
            if (sotish < tannarx && sotish > 0) {
                sotishInput.setCustomValidity('Sotish narxi tannarxdan past! Zarar ko‘rasiz.');
            } else {
                sotishInput.setCustomValidity('');
            }
        }
        tannarxInput.addEventListener('input', checkPrice);
        sotishInput.addEventListener('input', checkPrice);
    }
});