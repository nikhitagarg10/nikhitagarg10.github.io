# Generated by Django 4.0.5 on 2022-06-07 05:53

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fname', models.CharField(default='', max_length=50)),
                ('lname', models.CharField(default='', max_length=50)),
                ('Username', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
                ('adress', models.CharField(default='', max_length=100)),
                ('city', models.CharField(default='', max_length=20)),
                ('state', models.CharField(default='', max_length=20)),
                ('pincode', models.IntegerField(default=0, validators=[django.core.validators.MinValueValidator(6), django.core.validators.MaxValueValidator(6)])),
            ],
        ),
    ]