# Generated by Django 4.1.3 on 2023-01-27 07:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kAboom', '0036_alter_track_album_alter_track_until_price'),
    ]

    operations = [
        migrations.AddField(
            model_name='track',
            name='artist',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kAboom.artist'),
        ),
    ]