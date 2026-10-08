# Hotel Management System — 1-bosqich

O‘zbek tilidagi mehmonxona boshqaruv web-ilovasi. Ushbu bosqichda faqat login/logout, dashboard, xonalar va mehmonlar modullari mavjud.

## Talablar

- Python 3.10 yoki undan yangi
- pip

## Ishga tushirish

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt
python manage.py migrate
python manage.py runserver
```

Brauzerda `http://127.0.0.1:8000/` manzilini oching.

## Demo hisob

- **Username:** `admin`
- **Password:** `admin123`

Birinchi migratsiyadan so‘ng demo hisob, 20 ta xona va 10 ta mehmon SQLite bazasiga avtomatik qo‘shiladi. Mavjud demo ma’lumotlar takrorlanib yaratilmaydi.

> Demo login faqat mahalliy namoyish va ishlab chiqish uchun. Ommaviy muhitga joylashtirishdan oldin admin parolini almashtiring, `DJANGO_SECRET_KEY` ni sozlang va `DJANGO_DEBUG=0` qiling.

## Imkoniyatlar

- Username/parol bilan kirish va xavfsiz POST logout
- Database’dan hisoblanadigan jami, bo‘sh, band, ta’mirdagi xonalar va mehmonlar statistikasi
- Xonalar: qo‘shish, ko‘rish, tahrirlash, tasdiqlash bilan o‘chirish; card ko‘rinishi va rangli statuslar
- Mehmonlar: qo‘shish, ko‘rish, tahrirlash, tasdiqlash bilan o‘chirish va ism/familiya/telefon/passport/fuqarolik bo‘yicha qidiruv
- Responsive Bootstrap 5 interfeysi, SQLite ma’lumotlar bazasi

## Tekshiruv

```bash
python manage.py check
python manage.py test
```
