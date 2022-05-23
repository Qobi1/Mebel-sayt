from django import forms

from app1.models import Category


class CategoryForm(forms.ModelForm):
    class Meta:
        model = Category
        exclude = ['image_1', 'image_2']
        fields = '__all__'

