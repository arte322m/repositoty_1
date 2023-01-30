# Generated by Django 4.1.3 on 2023-01-27 07:10

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kAboom', '0035_rename_genres_track_genre'),
    ]

    operations = [
        migrations.AlterField(
            model_name='track',
            name='album',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='kAboom.album'),
        ),
        migrations.AlterField(
            model_name='track',
            name='until_price',
            field=models.FloatField(default=None, null=True),
        ),
    ]
