# Generated by Django 4.1.1 on 2022-10-12 20:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0005_project_project_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='SoftSkill',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=50)),
            ],
        ),
    ]