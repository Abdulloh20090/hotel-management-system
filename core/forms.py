from django import forms
from .models import Guest, Room


class BootstrapModelForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field in self.fields.values():
            css = "form-select" if isinstance(field.widget, forms.Select) else "form-control"
            field.widget.attrs["class"] = f'{field.widget.attrs.get("class", "")} {css}'.strip()
            field.widget.attrs.setdefault("placeholder", field.label)


class RoomForm(BootstrapModelForm):
    class Meta:
        model = Room
        fields = ["number", "floor", "room_type", "price", "capacity", "status"]
        widgets = {"price": forms.NumberInput(attrs={"step": "1000", "min": "0"})}


class GuestForm(BootstrapModelForm):
    class Meta:
        model = Guest
        fields = ["first_name", "last_name", "phone", "passport_id", "birth_date", "gender", "citizenship", "address"]
        widgets = {"birth_date": forms.DateInput(attrs={"type": "date"})}
