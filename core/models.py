from django.core.validators import MinValueValidator
from django.db import models


class Room(models.Model):
    class RoomType(models.TextChoices):
        SINGLE = "single", "Single"
        DOUBLE = "double", "Double"
        TWIN = "twin", "Twin"
        DELUXE = "deluxe", "Deluxe"
        SUITE = "suite", "Suite"

    class Status(models.TextChoices):
        AVAILABLE = "available", "Bo‘sh"
        OCCUPIED = "occupied", "Band"
        MAINTENANCE = "maintenance", "Ta’mirda"
        CLEANING = "cleaning", "Tozalanmoqda"

    number = models.CharField("Xona raqami", max_length=12, unique=True)
    floor = models.PositiveSmallIntegerField("Qavat", validators=[MinValueValidator(1)])
    room_type = models.CharField("Xona turi", max_length=12, choices=RoomType.choices)
    price = models.DecimalField("Narxi (so‘m)", max_digits=12, decimal_places=2, validators=[MinValueValidator(0)])
    capacity = models.PositiveSmallIntegerField("Sig‘imi", validators=[MinValueValidator(1)])
    status = models.CharField("Status", max_length=16, choices=Status.choices, default=Status.AVAILABLE)
    created_at = models.DateTimeField("Yaratilgan vaqt", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan vaqt", auto_now=True)

    class Meta:
        ordering = ["number"]
        verbose_name = "Xona"
        verbose_name_plural = "Xonalar"

    def __str__(self):
        return f"Xona {self.number}"


class Guest(models.Model):
    class Gender(models.TextChoices):
        MALE = "male", "Erkak"
        FEMALE = "female", "Ayol"

    first_name = models.CharField("Ism", max_length=80)
    last_name = models.CharField("Familiya", max_length=80)
    phone = models.CharField("Telefon", max_length=30)
    passport_id = models.CharField("Passport / ID", max_length=40, unique=True)
    birth_date = models.DateField("Tug‘ilgan sana")
    gender = models.CharField("Jinsi", max_length=8, choices=Gender.choices)
    citizenship = models.CharField("Fuqaroligi", max_length=80, default="O‘zbekiston")
    address = models.CharField("Manzil", max_length=240)
    created_at = models.DateTimeField("Yaratilgan vaqt", auto_now_add=True)
    updated_at = models.DateTimeField("Yangilangan vaqt", auto_now=True)

    class Meta:
        ordering = ["last_name", "first_name"]
        verbose_name = "Mehmon"
        verbose_name_plural = "Mehmonlar"

    def __str__(self):
        return f"{self.first_name} {self.last_name}"
