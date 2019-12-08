
from django.db import migrations


def get_status_building(apps, schema_editor):
    Flat = apps.get_model('property', 'Flat')
    for flat in Flat.objects.filter(construction_year__gte=2015):
        Flat.objects.update_or_create(new_building=True)


class Migration(migrations.Migration):

    dependencies = [
        ('property', '0004_auto_20191117_1849'),
    ]

    operations = [
        migrations.RunPython(get_status_building),
    ]

print()