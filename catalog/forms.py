from django import forms

from catalog.models import Product


class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ("name", "price", "description", "is_available", "image")

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
