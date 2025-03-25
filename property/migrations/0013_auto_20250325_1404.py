# Generated by Django 4.2.20 on 2025-03-25 07:04

from django.db import migrations


def link_owners_to_flats(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    Owner = apps.get_model('property', 'Owner')

    for flat in Flat.objects.all():
        if not flat.owner:
            continue

        owner = Owner.objects.filter(
            name=flat.owner,
            phonenumber=flat.owners_phonenumber,
            pure_phonenumber=flat.owner_pure_phone
        ).first()

        if owner:
            owner.flats.add(flat)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0012_auto_20250325_1335'),
    ]

    operations = [
        migrations.RunPython(link_owners_to_flats)
    ]
