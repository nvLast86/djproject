from django import forms
from catalog.models import Product


class ProductForm(forms.ModelForm):
    forbidden_words = ['казино', 'криптовалюта', 'крипта', 'биржа', 'дешево', 'бесплатно', 'обман', 'полиция', 'радар']

    class Meta:
        model = Product
        fields = ('title', 'description', 'image', 'category', 'price',)

    def clean_name(self):
        cleaned_name = self.cleaned_data['title']
        for word in self.forbidden_words:
            if word in cleaned_name.lower():
                raise forms.ValidationError(f'Название не может содержать слово "{word}"')
        return cleaned_name

    def clean_description(self):
        cleaned_description = self.cleaned_data['description']
        for word in self.forbidden_words:
            if word in cleaned_description.lower():
                raise forms.ValidationError(f'Описание не может содержать слово "{word}"')
        return cleaned_description

