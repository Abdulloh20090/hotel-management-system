from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.db.models import Q
from django.shortcuts import get_object_or_404, redirect, render
from django.views.decorators.http import require_POST
from .forms import GuestForm, RoomForm
from .models import Guest, Room


def login_page(request):
    from django.contrib.auth.views import LoginView
    return LoginView.as_view(template_name="core/login.html", redirect_authenticated_user=True)(request)


@login_required
def dashboard(request):
    stats = {
        "total_rooms": Room.objects.count(),
        "available_rooms": Room.objects.filter(status=Room.Status.AVAILABLE).count(),
        "occupied_rooms": Room.objects.filter(status=Room.Status.OCCUPIED).count(),
        "maintenance_rooms": Room.objects.filter(status=Room.Status.MAINTENANCE).count(),
        "total_guests": Guest.objects.count(),
    }
    recent_rooms = Room.objects.all()[:6]
    return render(request, "core/dashboard.html", {"stats": stats, "recent_rooms": recent_rooms})


@login_required
def room_list(request):
    rooms = Room.objects.all()
    return render(request, "core/room_list.html", {"rooms": rooms})


@login_required
def room_create(request):
    form = RoomForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Xona muvaffaqiyatli qo‘shildi.")
        return redirect("rooms")
    return render(request, "core/form.html", {"form": form, "title": "Yangi xona", "back_url": "rooms"})


@login_required
def room_update(request, pk):
    room = get_object_or_404(Room, pk=pk)
    form = RoomForm(request.POST or None, instance=room)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Xona ma’lumotlari yangilandi.")
        return redirect("rooms")
    return render(request, "core/form.html", {"form": form, "title": f"Xona {room.number}ni tahrirlash", "back_url": "rooms"})


@login_required
def room_delete(request, pk):
    room = get_object_or_404(Room, pk=pk)
    if request.method == "POST":
        room.delete()
        messages.success(request, "Xona o‘chirildi.")
        return redirect("rooms")
    return render(request, "core/confirm_delete.html", {"object": room, "object_label": "xonani", "back_url": "rooms"})


@login_required
def guest_list(request):
    query = request.GET.get("q", "").strip()
    guests = Guest.objects.all()
    if query:
        guests = guests.filter(
            Q(first_name__icontains=query) | Q(last_name__icontains=query) |
            Q(phone__icontains=query) | Q(passport_id__icontains=query) |
            Q(citizenship__icontains=query)
        )
    return render(request, "core/guest_list.html", {"guests": guests, "query": query})


@login_required
def guest_create(request):
    form = GuestForm(request.POST or None)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Mehmon muvaffaqiyatli qo‘shildi.")
        return redirect("guests")
    return render(request, "core/form.html", {"form": form, "title": "Yangi mehmon", "back_url": "guests"})


@login_required
def guest_update(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    form = GuestForm(request.POST or None, instance=guest)
    if request.method == "POST" and form.is_valid():
        form.save()
        messages.success(request, "Mehmon ma’lumotlari yangilandi.")
        return redirect("guests")
    return render(request, "core/form.html", {"form": form, "title": f"{guest}ni tahrirlash", "back_url": "guests"})


@login_required
def guest_delete(request, pk):
    guest = get_object_or_404(Guest, pk=pk)
    if request.method == "POST":
        guest.delete()
        messages.success(request, "Mehmon o‘chirildi.")
        return redirect("guests")
    return render(request, "core/confirm_delete.html", {"object": guest, "object_label": "mehmonni", "back_url": "guests"})
