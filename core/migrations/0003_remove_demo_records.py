from datetime import date
from decimal import Decimal
from django.conf import settings
from django.contrib.auth.hashers import check_password
from django.db import migrations


def remove_unchanged_demo_records(apps, schema_editor):
    db = schema_editor.connection.alias
    User = apps.get_model(*settings.AUTH_USER_MODEL.split("."))
    Room = apps.get_model("core", "Room")
    Guest = apps.get_model("core", "Guest")

    # Faqat o‘zgartirilmagan demo xonalarni o‘chiramiz; foydalanuvchi tahrirlagan
    # yoki o‘zi kiritgan ma’lumotlarga tegmaymiz.
    types = ["single", "double", "twin", "deluxe", "suite"]
    statuses = ["available", "occupied", "maintenance", "cleaning"]
    prices = {"single": Decimal("300000"), "double": Decimal("450000"), "twin": Decimal("480000"), "deluxe": Decimal("650000"), "suite": Decimal("900000")}
    for i in range(20):
        number = str(101 + i)
        room_type = types[i % len(types)]
        expected = {
            "floor": 1 + i // 7,
            "room_type": room_type,
            "price": prices[room_type],
            "capacity": 1 if room_type == "single" else (3 if room_type == "suite" else 2),
            "status": statuses[i % len(statuses)],
        }
        room = Room.objects.using(db).filter(number=number).first()
        if room and all(getattr(room, key) == value for key, value in expected.items()):
            room.delete(using=db)

    demo_guests = [
        ("Aziz", "Karimov", "+998901000101", "AA1000101", date(1990, 2, 14), "male", "O‘zbekiston", "Toshkent shahri"),
        ("Dilnoza", "Rasulova", "+998901000102", "AA1000102", date(1995, 7, 22), "female", "O‘zbekiston", "Samarqand shahri"),
        ("Jasur", "Tursunov", "+998901000103", "AA1000103", date(1988, 11, 3), "male", "O‘zbekiston", "Buxoro shahri"),
        ("Madina", "Yusupova", "+998901000104", "AA1000104", date(1998, 4, 17), "female", "O‘zbekiston", "Andijon shahri"),
        ("Bekzod", "Ismoilov", "+998901000105", "AA1000105", date(1985, 9, 9), "male", "O‘zbekiston", "Farg‘ona shahri"),
        ("Sevara", "Nazarova", "+998901000106", "AA1000106", date(1993, 12, 28), "female", "O‘zbekiston", "Qarshi shahri"),
        ("Akmal", "Rahimov", "+998901000107", "AA1000107", date(1991, 6, 5), "male", "O‘zbekiston", "Namangan shahri"),
        ("Mohira", "Abdullayeva", "+998901000108", "AA1000108", date(1997, 3, 12), "female", "O‘zbekiston", "Xiva shahri"),
        ("Sardor", "Qodirov", "+998901000109", "AA1000109", date(1987, 1, 30), "male", "O‘zbekiston", "Nukus shahri"),
        ("Nilufar", "Saidova", "+998901000110", "AA1000110", date(1994, 10, 19), "female", "O‘zbekiston", "Termiz shahri"),
    ]
    for first, last, phone, passport, birth, gender, citizenship, address in demo_guests:
        guest = Guest.objects.using(db).filter(passport_id=passport).first()
        expected = {
            "first_name": first, "last_name": last, "phone": phone,
            "birth_date": birth, "gender": gender,
            "citizenship": citizenship, "address": address,
        }
        if guest and all(getattr(guest, key) == value for key, value in expected.items()):
            guest.delete(using=db)

    demo_admin = User.objects.using(db).filter(username="admin").first()
    if demo_admin and not demo_admin.is_staff and not demo_admin.is_superuser and check_password("admin123", demo_admin.password):
        demo_admin.delete(using=db)


def preserve_records(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [("core", "0002_demo_data")]
    operations = [migrations.RunPython(remove_unchanged_demo_records, preserve_records)]
