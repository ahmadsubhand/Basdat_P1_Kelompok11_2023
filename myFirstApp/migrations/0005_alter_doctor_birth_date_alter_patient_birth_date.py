# Generated by Django 4.1.6 on 2023-11-02 09:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('myFirstApp', '0004_reservation_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doctor',
            name='birth_date',
            field=models.DateField(blank=True, default='2003-10-02', null=True),
        ),
        migrations.AlterField(
            model_name='patient',
            name='birth_date',
            field=models.DateField(blank=True, default='2003-10-02', null=True),
        ),
    ]
