# Generated by Django 5.0.6 on 2024-06-14 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0011_tbl_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tbl_shop',
            name='shop_address',
            field=models.CharField(max_length=100),
        ),
    ]
