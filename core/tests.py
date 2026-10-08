from datetime import date
from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from .models import Guest, Room


class HotelManagementTests(TestCase):
    def setUp(self):
        # Har bir test uchun migratsiya orqali kelgan demo yozuvlardan alohida toza holat.
        Room.objects.all().delete()
        Guest.objects.all().delete()
        self.user = get_user_model().objects.create_user(username="operator", password="Strong-test-123")

    def test_dashboard_requires_login_and_uses_database_counts(self):
        self.assertRedirects(self.client.get(reverse("dashboard")), "/login/?next=/")
        self.client.login(username="operator", password="Strong-test-123")
        Room.objects.create(number="301", floor=3, room_type=Room.RoomType.DOUBLE, price=450000, capacity=2, status=Room.Status.AVAILABLE)
        Room.objects.create(number="302", floor=3, room_type=Room.RoomType.SUITE, price=800000, capacity=3, status=Room.Status.MAINTENANCE)
        Guest.objects.create(first_name="Ali", last_name="Valiyev", phone="+998901112233", passport_id="AA1234567", birth_date=date(1990, 1, 1), gender=Guest.Gender.MALE, citizenship="O‘zbekiston", address="Toshkent")
        response = self.client.get(reverse("dashboard"))
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.context["stats"]["total_rooms"], 2)
        self.assertEqual(response.context["stats"]["available_rooms"], 1)
        self.assertEqual(response.context["stats"]["maintenance_rooms"], 1)
        self.assertEqual(response.context["stats"]["total_guests"], 1)

    def test_room_create_edit_and_confirmed_delete(self):
        self.client.login(username="operator", password="Strong-test-123")
        payload = {"number": "401", "floor": "4", "room_type": Room.RoomType.SINGLE, "price": "300000", "capacity": "1", "status": Room.Status.AVAILABLE}
        response = self.client.post(reverse("room_create"), payload)
        self.assertRedirects(response, reverse("rooms"))
        room = Room.objects.get(number="401")
        payload["status"] = Room.Status.OCCUPIED
        response = self.client.post(reverse("room_edit", args=[room.pk]), payload)
        self.assertRedirects(response, reverse("rooms"))
        room.refresh_from_db()
        self.assertEqual(room.status, Room.Status.OCCUPIED)
        self.assertEqual(self.client.get(reverse("room_delete", args=[room.pk])).status_code, 200)
        response = self.client.post(reverse("room_delete", args=[room.pk]))
        self.assertRedirects(response, reverse("rooms"))
        self.assertFalse(Room.objects.filter(pk=room.pk).exists())

    def test_guest_create_search_and_delete(self):
        self.client.login(username="operator", password="Strong-test-123")
        payload = {"first_name": "Dilnoza", "last_name": "Karimova", "phone": "+998901234567", "passport_id": "AB7654321", "birth_date": "1995-06-15", "gender": Guest.Gender.FEMALE, "citizenship": "O‘zbekiston", "address": "Samarqand"}
        response = self.client.post(reverse("guest_create"), payload)
        self.assertRedirects(response, reverse("guests"))
        response = self.client.get(reverse("guests"), {"q": "Dilnoza"})
        self.assertContains(response, "Dilnoza Karimova")
        self.assertEqual(len(response.context["guests"]), 1)
        guest = Guest.objects.get(passport_id="AB7654321")
        self.client.post(reverse("guest_delete", args=[guest.pk]))
        self.assertFalse(Guest.objects.filter(pk=guest.pk).exists())

    def test_login_page_and_demo_credentials_are_available_after_migrations(self):
        response = self.client.get(reverse("login"))
        self.assertEqual(response.status_code, 200)
        self.assertTrue(get_user_model().objects.filter(username="admin").exists())
        self.assertTrue(self.client.login(username="admin", password="admin123"))
        self.assertEqual(self.client.get(reverse("dashboard")).status_code, 200)
