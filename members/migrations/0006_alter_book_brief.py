# Generated by Django 4.1.5 on 2023-02-02 17:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0005_reading'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='brief',
            field=models.CharField(max_length=255),
        ),
    ]
