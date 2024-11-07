from django.core.exceptions import ValidationError
from django.forms import ModelForm, BooleanField

from .models import Product


class StyleFormMixin:
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StyleFormMixin, ModelForm):
    banned_words = [
        "казино",
        "криптовалюта",
        "крипта",
        "биржа",
        "дешево",
        "бесплатно",
        "обман",
        "полиция",
        "радар",
    ]

    class Meta:
        model = Product
        fields = "__all__"

    def clean_name(self):
        name = self.cleaned_data.get("name")
        for banned_word in self.banned_words:
            if banned_word in name.lower():
                raise ValidationError(
                    f'"{banned_word}" Данное слово запрещено к использованию.'
                )
        return name

    def clean_description(self):
        description = self.cleaned_data.get("description")
        for banned_word in self.banned_words:
            if banned_word in description.lower():
                raise ValidationError(
                    f'"{banned_word}" Данное слово запрещено к использованию.'
                )
        return description

    def clean_price(self):
        price = self.cleaned_data.get("price")
        if price < 0:
            raise ValidationError("Цена не может быть отрицательной")
        return price

    def clean_image(self):
        image = self.cleaned_data.get("image")
        if image:
            if not (
                    image.name.lower().endswith(".jpg")
                    or image.name.lower().endswith(".jpeg")
                    or image.name.lower().endswith(".png")
            ):
                raise ValidationError("Только JPEG и PNG файлы разрешены.")

            if image.size > 5 * 1024 * 1024:  # 5 МБ в байтах
                raise ValidationError("Размер файла не должен превышать 5 МБ.")

        return image
