# Generated by Django 3.2.9 on 2021-11-22 07:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clans', '0002_auto_20211122_1238'),
    ]

    operations = [
        migrations.RenameField(
            model_name='contact',
            old_name='desc',
            new_name='gender',
        ),
        migrations.AlterField(
            model_name='contact',
            name='admission',
            field=models.IntegerField(default='', max_length=10),
        ),
    ]
