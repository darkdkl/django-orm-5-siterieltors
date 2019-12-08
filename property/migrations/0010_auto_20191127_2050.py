# Generated by Django 2.2.4 on 2019-11-27 17:50

from django.db import migrations
import phonenumbers


def get_pure(number):
    pure_number = phonenumbers.parse(number, 'RU')
    if phonenumbers.is_valid_number(pure_number):
        return f'+{pure_number.country_code}{pure_number.national_number}'
    else:
        return None


def get_owner_phone_pure(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.all():
        pure_number = get_pure(flat.owners_phonenumber)
        if pure_number:
            Flat.objects.update_or_create(town=flat.town, address=flat.address, price=flat.price, defaults={
                'owner_phone_pure': pure_number})


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0009_flat_owner_phone_pure'),
    ]

    operations = [
        migrations.RunPython(get_owner_phone_pure),
    ]
