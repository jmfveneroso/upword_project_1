# Generated by Django 3.2.3 on 2022-06-19 20:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('senior_panel', '0002_calendarentry'),
    ]

    operations = [
        migrations.AddField(
            model_name='userinfo',
            name='status',
            field=models.CharField(default='idle', max_length=200),
        ),
    ]