# Generated by Django 2.2.17 on 2021-01-13 06:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bookstore', '0002_auto_20210112_1049'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='book',
            options={'verbose_name': '图书', 'verbose_name_plural': '图书'},
        ),
    ]
