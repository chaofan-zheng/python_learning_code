# Generated by Django 2.2.17 on 2021-03-05 09:56

from django.db import migrations
import tinymce.models


class Migration(migrations.Migration):

    dependencies = [
        ('goods', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='goodstest',
            options={'verbose_name': '商品', 'verbose_name_plural': '商品'},
        ),
        migrations.AlterField(
            model_name='goodstest',
            name='detail',
            field=tinymce.models.HTMLField(verbose_name='商品详情'),
        ),
    ]
