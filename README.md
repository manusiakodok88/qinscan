# BMG Scanner 🔍

BMG Scanner adalah tool berbasis Flask untuk melakukan scan keamanan dasar website berbasis WordPress. Mendukung:
- Deteksi versi WordPress dan plugin
- Pencarian CVE otomatis + AI Summary
- Export hasil scan ke CSV
- Riwayat scan & sistem login multi-user
- Monetisasi via manual upgrade Telegram

## 🚀 Fitur Utama
- Login/Register dengan proteksi JWT
- Limit scan harian berdasarkan plan (free, basic, pro)
- Dashboard UI full responsive
- Admin Panel: upgrade plan langsung
- Telegram Manual Upgrade (bukan Stripe)

## 🧪 Cara Jalan Lokal
```bash
pip install -r requirements.txt
python app.py
```

## 🛠 Deployment
Gunakan Gunicorn + NGINX untuk VPS, atau Render jika tanpa custom domain.

## 👤 Admin Panel
Akses halaman `admin_panel.html` jika login sebagai role `admin`.

## 🔐 Konfigurasi ENV
Buat file `.env` berdasarkan `.env.example`:
```
SECRET_KEY=isi_rahasiamu
```

## 👥 Kontribusi
Pull request, issue, dan diskusi terbuka. Hubungi admin via [Telegram](https://t.me/Sentogal) untuk upgrade akun.

---

© BackM Group | BMGScanner v1.0
