# Generated by Django 2.2.7 on 2019-12-01 16:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('members', '0015_remove_position_active'),
    ]

    operations = [
        migrations.AlterField(
            model_name='member',
            name='city',
            field=models.CharField(blank=True, max_length=64),
        ),
    ]
