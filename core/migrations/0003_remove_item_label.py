# Generated by Django 2.2 on 2021-07-15 16:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20210715_2225'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='item',
            name='label',
        ),
    ]