# Generated by Django 4.1.1 on 2022-10-14 20:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0008_experience_end_date_alter_experience_start_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='experience',
            name='work',
            field=models.BooleanField(default=False),
        ),
    ]
