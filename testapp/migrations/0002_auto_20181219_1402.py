# Generated by Django 2.1.4 on 2018-12-19 14:02

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('testapp', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='account',
            old_name='name',
            new_name='username',
        ),
    ]