# Generated by Django 2.0.3 on 2018-03-23 17:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20180323_1300'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user',
            old_name='confirmed',
            new_name='is_confirmed',
        ),
    ]