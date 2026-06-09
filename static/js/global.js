// global.js
document.addEventListener('DOMContentLoaded', function() {
    // Sidebar toggles (faqat authenticated user sahifasida mavjud bo‘lsa)
    const sidebar = document.getElementById('sidebar');
    const openBtn = document.getElementById('openSidebarBtn');
    const closeBtn = document.getElementById('closeSidebarBtn');

    if (sidebar && openBtn) {
        openBtn.addEventListener('click', () => {
            sidebar.classList.remove('-translate-x-full');
        });
    }
    if (sidebar && closeBtn) {
        closeBtn.addEventListener('click', () => {
            sidebar.classList.add('-translate-x-full');
        });
    }

    // Delete konfirmatsiyasi (.confirm-delete classli elementlar uchun)
    document.querySelectorAll('.confirm-delete').forEach(btn => {
        btn.addEventListener('click', (e) => {
            if (!confirm('Haqiqatan ham o‘chirmoqchimisiz?')) {
                e.preventDefault();
            }
        });
    });

    // Xabarlarni avtomatik yashirish (5 sekund)
    setTimeout(() => {
        document.querySelectorAll('.bg-green-100, .bg-blue-100').forEach(msg => {
            msg.style.transition = 'opacity 0.5s';
            msg.style.opacity = '0';
            setTimeout(() => msg.remove(), 500);
        });
    }, 5000);
});