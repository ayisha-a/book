from django.forms import ModelForm
from .models import BOOK

class BookCreateForm(ModelForm):
    class Meta:
        model=BOOK
        fields="__all__"