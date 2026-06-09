// static/js/analytics.js
document.addEventListener('DOMContentLoaded', function () {
    // Filtrlarni avtomatik yuborish (sana o'zgartirilganda)
    const startInput = document.getElementById('start_date');
    const endInput = document.getElementById('end_date');
    const filterForm = document.getElementById('analytics-filter-form');

    function submitForm() {
        if (startInput.value && endInput.value) {
            filterForm.submit();
        }
    }
    if (startInput && endInput) {
        startInput.addEventListener('change', submitForm);
        endInput.addEventListener('change', submitForm);
    }

    // Tozalash tugmasi (reset)
    const resetBtn = document.getElementById('reset-btn');
    if (resetBtn) {
        resetBtn.addEventListener('click', function (e) {
            e.preventDefault();
            window.location.href = window.location.pathname;
        });
    }

    // 1. Trend chizig'i (Revenue va Profit)
    const labels = JSON.parse(document.getElementById('chart-labels').textContent);
    const revenueData = JSON.parse(document.getElementById('chart-revenue').textContent);
    const profitData = JSON.parse(document.getElementById('chart-profit').textContent);

    const ctx = document.getElementById('trendChart').getContext('2d');
    new Chart(ctx, {
        type: 'line',
        data: {
            labels: labels,
            datasets: [
                {
                    label: 'Tushum (so\'m)',
                    data: revenueData,
                    borderColor: '#4f46e5',
                    backgroundColor: 'rgba(79, 70, 229, 0.05)',
                    tension: 0.3,
                    fill: true,
                    yAxisID: 'y'
                },
                {
                    label: 'Foyda (so\'m)',
                    data: profitData,
                    borderColor: '#10b981',
                    backgroundColor: 'rgba(16, 185, 129, 0.05)',
                    tension: 0.3,
                    fill: true,
                    yAxisID: 'y'
                }
            ]
        },
        options: {
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                tooltip: { mode: 'index', intersect: false },
                legend: { position: 'top' }
            },
            scales: {
                y: { title: { display: true, text: 'So\'m' } }
            }
        }
    });

    // 2. Top 5 mahsulot gorizontal bar chart
    const topProducts = JSON.parse(document.getElementById('top-products').textContent);
    const productNames = topProducts.map(p => p.product__name + (p.product__color ? ` (${p.product__color})` : ''));
    const productQtys = topProducts.map(p => p.total_qty);

    const ctxBar = document.getElementById('topProductsChart').getContext('2d');
    new Chart(ctxBar, {
        type: 'bar',
        data: {
            labels: productNames,
            datasets: [{
                label: 'Sotilgan miqdor (dona)',
                data: productQtys,
                backgroundColor: '#f59e0b',
                borderRadius: 6,
                barPercentage: 0.6
            }]
        },
        options: {
            indexAxis: 'y',
            responsive: true,
            maintainAspectRatio: true,
            plugins: {
                legend: { position: 'top' }
            }
        }
    });
});