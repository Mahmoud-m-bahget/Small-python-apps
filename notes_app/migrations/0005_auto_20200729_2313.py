# Generated by Django 3.0.3 on 2020-07-29 21:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('notes_app', '0004_auto_20200729_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='note',
            name='img',
            field=models.ImageField(upload_to='notes-img'),
        ),
    ]
