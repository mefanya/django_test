from django import forms

from catalog.models import Product


class StileFormMixin:
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)
        for fild_name, field in self.fields.items():
            if isinstance(field, forms.BooleanField):
                field.widget.attrs["class"] = "form-check-input"
            else:
                field.widget.attrs["class"] = "form-control"


class ProductForm(StileFormMixin, forms.ModelForm):

    class Meta:
        model = Product
        exclude = ("views_count",)

    def clean_name(self):
        forbidden_words = [
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

        cleaned_data = self.cleaned_data.get("name")
        data = cleaned_data.lower().split()
        words_list = set(data).intersection(forbidden_words)

        if words_list:
            raise forms.ValidationError(
                "Извините, но нельзя использовать запрещенные слова в названии продукта."
            )

        return cleaned_data
