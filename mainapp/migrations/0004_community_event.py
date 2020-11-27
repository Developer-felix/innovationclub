# Generated by Django 2.2.16 on 2020-11-20 08:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mainapp', '0003_marketpost'),
    ]

    operations = [
        migrations.CreateModel(
            name='Community_Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('venue', models.CharField(max_length=100)),
                ('event_date', models.DateTimeField()),
                ('image', models.ImageField(upload_to='event_images')),
                ('time_start', models.DateTimeField(auto_now_add=True)),
                ('time_end', models.DateTimeField()),
                ('community', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mainapp.Community')),
            ],
        ),
    ]
