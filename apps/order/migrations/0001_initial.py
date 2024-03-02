# Generated by Django 5.0.2 on 2024-03-02 15:02

import datetime
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status', models.IntegerField(choices=[(1, 'have_done'), (2, 'hevent_done')])),
                ('address', models.CharField(max_length=100)),
                ('created_add', models.DateField(auto_now_add=True)),
                ('start_time', models.DateField(default=datetime.datetime(2024, 3, 2, 15, 2, 55, 1653, tzinfo=datetime.timezone.utc))),
                ('id_employer', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='employer', to='user.user')),
                ('id_worker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='worker', to='user.user')),
            ],
        ),
    ]
