# Generated by Django 2.1.7 on 2019-06-13 06:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('order', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='order',
            old_name='first_name',
            new_name='username',
        ),
        migrations.RemoveField(
            model_name='order',
            name='last_name',
        ),
    ]