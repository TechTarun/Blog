# Generated by Django 3.1.2 on 2021-05-30 12:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='img',
            field=models.ImageField(default='hi.png', upload_to='user_pics'),
        ),
    ]