# Generated by Django 3.2.10 on 2022-09-05 16:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='booking',
            old_name='active',
            new_name='booked',
        ),
    ]