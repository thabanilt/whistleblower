# Generated by Django 2.1.4 on 2019-01-10 05:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users_auth', '0008_customuser_image'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='notifications',
            field=models.IntegerField(default=0),
        ),
    ]
