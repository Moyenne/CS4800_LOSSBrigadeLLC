# Generated by Django 3.1.7 on 2021-05-14 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0003_auto_20210513_2134'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='emailAddress',
            field=models.CharField(max_length=255),
        ),
    ]