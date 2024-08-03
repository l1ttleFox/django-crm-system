# Generated by Django 5.0.7 on 2024-08-03 01:18

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('ads', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Lead',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('first_name', models.CharField(max_length=50, verbose_name='First name')),
                ('last_name', models.CharField(max_length=50, verbose_name='Last name')),
                ('phone_number', models.CharField(blank=True, max_length=20, verbose_name='Phone number')),
                ('email', models.EmailField(blank=True, max_length=254, verbose_name='Email')),
                ('advertising_campaign', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='leads', to='ads.advertisement', verbose_name='The campaign user came from')),
            ],
            options={
                'ordering': ['pk'],
            },
        ),
    ]