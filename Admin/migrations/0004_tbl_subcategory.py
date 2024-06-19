# Generated by Django 5.0.6 on 2024-06-13 10:28

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Admin', '0003_tbl_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='tbl_subcategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('subcategory_name', models.CharField(max_length=30)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Admin.tbl_category')),
            ],
        ),
    ]