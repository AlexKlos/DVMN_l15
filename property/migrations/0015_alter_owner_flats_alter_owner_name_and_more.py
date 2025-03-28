# Generated by Django 4.2.20 on 2025-03-25 07:25

from django.db import migrations, models
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0014_remove_flat_owner_pure_phone_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner',
            name='flats',
            field=models.ManyToManyField(blank=True, db_index=True, related_name='owners', to='property.flat', verbose_name='Квартиры в собственности'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='name',
            field=models.CharField(db_index=True, max_length=200, verbose_name='ФИО владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='phonenumber',
            field=models.CharField(blank=True, db_index=True, max_length=20, verbose_name='Номер владельца'),
        ),
        migrations.AlterField(
            model_name='owner',
            name='pure_phonenumber',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, db_index=True, max_length=128, region='RU', verbose_name='Нормализованный номер владельца'),
        ),
    ]
