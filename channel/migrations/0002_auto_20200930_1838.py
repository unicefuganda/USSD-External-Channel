# Generated by Django 3.1.1 on 2020-09-30 18:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('channel', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ussdsession',
            name='last_access_at',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
