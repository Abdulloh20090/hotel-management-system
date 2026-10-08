from django.utils import timezone
from .models import Room


def sidebar_data(request):
    return {
        "today": timezone.localdate(),
        "sidebar_room_count": Room.objects.count() if request.user.is_authenticated else 0,
    }
