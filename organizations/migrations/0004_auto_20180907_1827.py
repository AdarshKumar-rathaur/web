# Generated by Django 2.1 on 2018-09-07 17:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('organizations', '0003_membership_joint_organization'),
    ]

    operations = [
        migrations.AddField(
            model_name='organizationcategory',
            name='display_name',
            field=models.CharField(blank=True, max_length=256),
        ),
        migrations.AddField(
            model_name='organizationrole',
            name='display_name',
            field=models.CharField(blank=True, max_length=256),
        ),
    ]
