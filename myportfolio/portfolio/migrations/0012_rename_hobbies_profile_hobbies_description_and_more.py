# Generated by Django 4.1.1 on 2022-10-25 20:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portfolio', '0011_profile_alter_experience_end_date_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='profile',
            old_name='hobbies',
            new_name='hobbies_description',
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_picture',
            field=models.ImageField(default='./static/images/profile-pictures/pp-1.jpg', upload_to='images/profile-pictures/'),
        ),
    ]
