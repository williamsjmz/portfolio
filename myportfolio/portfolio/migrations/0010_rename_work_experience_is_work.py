# Generated by Django 4.1.1 on 2022-10-14 20:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0009_experience_work'),
    ]

    operations = [
        migrations.RenameField(
            model_name='experience',
            old_name='work',
            new_name='is_work',
        ),
    ]