# Generated by Django 2.1 on 2018-08-25 17:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=256)),
                ('slug', models.SlugField(unique=True)),
                ('active', models.BooleanField(default=False, help_text='The current event is shown in the events page')),
                ('opened_ticket_sales', models.BooleanField(default=False)),
                ('start_date', models.DateField()),
                ('default_slot_duration', models.DurationField(default=3000)),
                ('short_description', models.TextField(blank=True)),
                ('description', models.TextField(blank=True, help_text='Markdown is allowed')),
                ('cover', models.ImageField(blank=True, upload_to='events/event/')),
                ('poster', models.FileField(blank=True, upload_to='events/event/')),
                ('sponsorship_brochure', models.FileField(blank=True, upload_to='events/event/')),
            ],
        ),
    ]
