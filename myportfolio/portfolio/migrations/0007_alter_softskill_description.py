# Generated by Django 4.1.1 on 2022-10-12 20:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0006_softskill'),
    ]

    operations = [
        migrations.AlterField(
            model_name='softskill',
            name='description',
            field=models.CharField(max_length=500),
        ),
    ]
