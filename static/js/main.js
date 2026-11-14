// AuraFolio JavaScript Interactions

document.addEventListener('DOMContentLoaded', () => {
    // 1. Live Cover Image Preview in Book Forms
    const coverUrlInput = document.getElementById('id_cover_url');
    const coverFileInput = document.getElementById('id_cover_image');
    const previewImg = document.getElementById('cover-preview-img');
    const previewPlaceholder = document.getElementById('cover-preview-placeholder');

    function updatePreview(src) {
        if (!previewImg || !previewPlaceholder) return;
        if (src) {
            previewImg.src = src;
            previewImg.classList.remove('d-none');
            previewPlaceholder.classList.add('d-none');
        } else {
            previewImg.classList.add('d-none');
            previewPlaceholder.classList.remove('d-none');
        }
    }

    if (coverUrlInput) {
        coverUrlInput.addEventListener('input', (e) => {
            const url = e.target.value.trim();
            if (url) {
                updatePreview(url);
            } else if (!coverFileInput || !coverFileInput.files.length) {
                updatePreview('');
            }
        });
    }

    if (coverFileInput) {
        coverFileInput.addEventListener('change', (e) => {
            if (e.target.files && e.target.files[0]) {
                const reader = new FileReader();
                reader.onload = (event) => {
                    updatePreview(event.target.result);
                };
                reader.readAsDataURL(e.target.files[0]);
            }
        });
    }

    // 2. Auto-fade Django Messages / Alerts after 5 seconds
    const alerts = document.querySelectorAll('.alert-dismissible');
    alerts.forEach(alert => {
        setTimeout(() => {
            try {
                const bsAlert = new bootstrap.Alert(alert);
                bsAlert.close();
            } catch (e) {
                alert.style.display = 'none';
            }
        }, 5000);
    });

    // 3. Navbar Scrolled Shadow
    const navbar = document.querySelector('.aesthetic-navbar');
    if (navbar) {
        window.addEventListener('scroll', () => {
            if (window.scrollY > 30) {
                navbar.classList.add('shadow-sm');
                navbar.style.background = 'rgba(250, 247, 242, 0.95)';
            } else {
                navbar.classList.remove('shadow-sm');
                navbar.style.background = 'rgba(250, 247, 242, 0.88)';
            }
        });
    }
});

