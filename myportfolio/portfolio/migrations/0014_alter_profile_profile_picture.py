# Generated by Django 4.1.1 on 2022-10-25 20:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0013_alter_profile_profile_picture'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='./static/images/profile-pictures/default-pp.jpg', upload_to='portfolio/static/images/profile-pictures/'),
        ),
    ]
