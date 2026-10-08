from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):
    # Backwards-compatible migration slot: demo fixtures are intentionally disabled.
    # Existing installs that already ran the previous version are cleaned safely by 0003.
    dependencies = [
        ("core", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]
    operations = []
