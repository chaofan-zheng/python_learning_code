# Generated by Django 2.2.17 on 2021-03-05 09:15

from django.db import migrations, models
import tinymce.models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='GoodsTest',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.SmallIntegerField(choices=[(0, '上架'), (1, '下架')], default=1, verbose_name='状态')),
                ('detail', tinymce.models.HTMLField(verbose_name='goods detail')),
            ],
            options={
                'db_table': 'df_goods_test',
            },
        ),
    ]