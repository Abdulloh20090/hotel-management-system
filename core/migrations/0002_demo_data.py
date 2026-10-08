from datetime import date
from django.conf import settings
from django.db import migrations


def add_demo_data(apps, schema_editor):
    User = apps.get_model(*settings.AUTH_USER_MODEL.split("."))
    Room = apps.get_model("core", "Room")
    Guest = apps.get_model("core", "Guest")
    db = schema_editor.connection.alias

    if not User.objects.using(db).filter(username="admin").exists():
        User.objects.db_manager(db).create_user(username="admin", password="admin123")

    room_types = ["single", "double", "twin", "deluxe", "suite"]
    statuses = ["available", "occupied", "maintenance", "cleaning"]
    prices = {"single": 300000, "double": 450000, "twin": 480000, "deluxe": 650000, "suite": 900000}
    for i in range(20):
        number = str(101 + i)
        room_type = room_types[i % len(room_types)]
        Room.objects.using(db).get_or_create(
            number=number,
            defaults={
                "floor": 1 + (i // 7),
                "room_type": room_type,
                "price": prices[room_type],
                "capacity": 1 if room_type == "single" else (3 if room_type == "suite" else 2),
                "status": statuses[i % len(statuses)],
            },
        )

    guests = [
        ("Aziz", "Karimov", "+998901000101", "AA1000101", "1990-02-14", "male", "O‘zbekiston", "Toshkent shahri"),
        ("Dilnoza", "Rasulova", "+998901000102", "AA1000102", "1995-07-22", "female", "O‘zbekiston", "Samarqand shahri"),
        ("Jasur", "Tursunov", "+998901000103", "AA1000103", "1988-11-03", "male", "O‘zbekiston", "Buxoro shahri"),
        ("Madina", "Yusupova", "+998901000104", "AA1000104", "1998-04-17", "female", "O‘zbekiston", "Andijon shahri"),
        ("Bekzod", "Ismoilov", "+998901000105", "AA1000105", "1985-09-09", "male", "O‘zbekiston", "Farg‘ona shahri"),
        ("Sevara", "Nazarova", "+998901000106", "AA1000106", "1993-12-28", "female", "O‘zbekiston", "Qarshi shahri"),
        ("Akmal", "Rahimov", "+998901000107", "AA1000107", "1991-06-05", "male", "O‘zbekiston", "Namangan shahri"),
        ("Mohira", "Abdullayeva", "+998901000108", "AA1000108", "1997-03-12", "female", "O‘zbekiston", "Xiva shahri"),
        ("Sardor", "Qodirov", "+998901000109", "AA1000109", "1987-01-30", "male", "O‘zbekiston", "Nukus shahri"),
        ("Nilufar", "Saidova", "+998901000110", "AA1000110", "1994-10-19", "female", "O‘zbekiston", "Termiz shahri"),
    ]
    for first, last, phone, passport, birth, gender, citizenship, address in guests:
        Guest.objects.using(db).get_or_create(
            passport_id=passport,
            defaults={
                "first_name": first,
                "last_name": last,
                "phone": phone,
                "birth_date": date.fromisoformat(birth),
                "gender": gender,
                "citizenship": citizenship,
                "address": address,
            },
        )


def keep_demo_data(apps, schema_editor):
    pass


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [migrations.RunPython(add_demo_data, keep_demo_data)]
