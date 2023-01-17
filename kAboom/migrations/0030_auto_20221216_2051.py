# Generated by Django 4.1.3 on 2022-12-16 17:51

from django.db import migrations


def data_migrate_user(apps, schema_editor):
    UserProfile = apps.get_model('kAboom', 'UserProfile')
    for user in UserProfile.objects.all():
        user.type_of_theme = 'DARK'
        user.save()


class Migration(migrations.Migration):

    dependencies = [
        ('kAboom', '0029_alter_userprofile_type_of_theme'),
        ('kAboom', '0026_userprofile_type_of_theme'),
    ]

    operations = [
        migrations.RunPython(data_migrate_user)
    ]