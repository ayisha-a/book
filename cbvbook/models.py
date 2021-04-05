from django.db import models

# Create your models here.
class BOOK(models.Model):
    book_name=models.CharField(max_length=120,unique=True)
    pages=models.IntegerField(default=50)
    price=models.IntegerField(default=50)
    author=models.CharField(max_length=120)

    def __str__(self):
        return self.book_name