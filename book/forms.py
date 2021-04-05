from django.forms import forms,ModelForm
from book.models import Book

class BookCreateForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"
    def clean(self):
        cleaned_data=super().clean()
        price=cleaned_data.get("price")
        pages=cleaned_data.get("pages")
        if price<50:
            msg="invalid price prove value >50"
            self.add_error("price",msg)
        if pages<30:
            msg = "invalid pages prove value >30"
            self.add_error("pages", msg)
class BookUpdateForm(ModelForm):
    class Meta:
        model=Book
        fields="__all__"