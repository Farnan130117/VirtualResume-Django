# Generated by Django 3.0.6 on 2020-07-03 15:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('base', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='picture',
            field=models.ImageField(null=True, upload_to=''),
        ),
    ]
