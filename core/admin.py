from django.contrib import admin
from .models import Guest, Room


@admin.register(Room)
class RoomAdmin(admin.ModelAdmin):
    list_display = ("number", "floor", "room_type", "price", "capacity", "status")
    list_filter = ("status", "room_type", "floor")
    search_fields = ("number",)


@admin.register(Guest)
class GuestAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "phone", "passport_id", "citizenship")
    search_fields = ("first_name", "last_name", "phone", "passport_id")
