# Generated by Django 4.2.4 on 2023-09-03 18:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0003_alter_trash_user'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Trash',
        ),
    ]
