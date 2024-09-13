# Generated by Django 5.0.6 on 2024-06-26 10:45

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('myadmin', '0001_initial'),
        ('user', '0002_delete_register'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Register',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.BigIntegerField()),
                ('dob', models.DateField()),
                ('gender', models.CharField(max_length=50)),
                ('address', models.TextField()),
                ('status', models.CharField(default='pending', max_length=255)),
                ('area', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.area')),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.city')),
                ('state', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myadmin.state')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'db_table': 'register',
            },
        ),
    ]
