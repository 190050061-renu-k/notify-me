# Generated by Django 3.1.4 on 2020-12-02 10:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dashboard', '0002_deadline'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='code',
            field=models.CharField(default='', max_length=10),
        ),
    ]
