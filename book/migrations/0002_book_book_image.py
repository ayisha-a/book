# Generated by Django 3.1.6 on 2021-02-23 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('book', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='book_image',
            field=models.ImageField(default='image1', upload_to='images'),
            preserve_default=False,
        ),
    ]
