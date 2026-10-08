# Hotel Management System — 1-bosqich

Xonalar va mehmonlar ma’lumotlarini SQLite bazasida **haqiqatan saqlaydigan**, CRUD amallari va login bilan ishlaydigan Django web-ilovasi. Yangi o‘rnatishda demo foydalanuvchi yoki namunaviy xona/mehmonlar yaratilmaydi. Ma’lumotlar faqat foydalanuvchi kiritgandan keyin saqlanadi.

## Talablar

- Python 3.10 yoki undan yangi
- pip

## Mahalliy ishga tushirish

```bash
python -m venv .venv
source .venv/bin/activate       # Windows: .venv\\Scripts\\activate
pip install -r requirements.txt

# Mahalliy muhit uchun kalit va debug rejimi
export DJANGO_SECRET_KEY="$(python -c 'import secrets; print(secrets.token_urlsafe(48))')"
export DJANGO_DEBUG=1
python manage.py migrate
python manage.py createsuperuser
python manage.py runserver
```

Windows PowerShell’da environment variable’larni `$env:DJANGO_SECRET_KEY = ...` va `$env:DJANGO_DEBUG = "1"` ko‘rinishida belgilang.

Brauzerda `http://127.0.0.1:8000/` ni ochib, `createsuperuser` vaqtida o‘zingiz yaratgan username va parol bilan kiring. Demo yoki umumiy parol ilovada saqlanmaydi.

## Ishlab chiqarish muhiti

Production server environment’ida quyidagilarni belgilang:

- `DJANGO_SECRET_KEY` — xavfsiz, tasodifiy va maxfiy kalit (kodga yoki Git’ga qo‘shmang)
- `DJANGO_DEBUG=0`
- `DJANGO_ALLOWED_HOSTS=example.com,www.example.com`
- `DJANGO_TRUST_X_FORWARDED_PROTO=1` — faqat reverse proxy `X-Forwarded-Proto` sarlavhasini ishonchli tarzda o‘rnatib/yangilab tursa

Standart production sozlamalari HTTP’dan HTTPS’ga yo‘naltiradi, xavfsiz session/CSRF cookie’larini qo‘llaydi va HSTS’ni yoqadi. HSTS domeningiz HTTPS orqali to‘liq ishlayotganiga ishonch hosil qilgandan keyingina yoqilgan holda qolsin. Hosting TLS’ni reverse proxy’da yakunlamasa, proxy sozlamasini moslang.

Serverda `python manage.py migrate`, bir marta `python manage.py createsuperuser` va statik fayllar uchun `python manage.py collectstatic --noinput` bajaring. WhiteNoise to‘plangan statik fayllarni ilovadan yetkazadi. SQLite bitta serverli kichik o‘rnatishga mo‘ljallangan; ko‘p foydalanuvchi va yuqori yuklama uchun PostgreSQL’ga o‘tish kerak.

## Ishlaydigan imkoniyatlar

- Login/logout; parollar Django tomonidan xeshlanadi
- Dashboard ko‘rsatkichlari bazadagi haqiqiy yozuvlardan hisoblanadi
- Xonalarni qo‘shish, ko‘rish, tahrirlash va o‘chirishdan oldin tasdiqlash
- Xonalar card ko‘rinishida va rangli status bilan
- Mehmonlarni qo‘shish, ko‘rish, tahrirlash, tasdiqlab o‘chirish va ism/familiya/telefon/passport/fuqarolik bo‘yicha qidirish
- Responsive Bootstrap interfeysi va SQLite’da doimiy saqlanadigan ma’lumotlar

## Tekshiruv

```bash
python manage.py check
python manage.py test
```
