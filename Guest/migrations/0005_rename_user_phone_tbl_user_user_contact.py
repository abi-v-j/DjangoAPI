# Generated by Django 5.0.6 on 2024-06-14 07:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Guest', '0004_tbl_user'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tbl_user',
            old_name='user_phone',
            new_name='user_contact',
        ),
    ]