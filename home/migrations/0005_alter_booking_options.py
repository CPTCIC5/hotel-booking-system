# Generated by Django 4.1 on 2022-09-06 07:56

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_auto_20220906_0113'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='booking',
            options={'ordering': ['-booked']},
        ),
    ]
