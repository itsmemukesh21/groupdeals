# Generated by Django 2.2.2 on 2019-06-05 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='customer',
            name='phonenumber',
            field=models.CharField(blank=True, max_length=12, null=True),
        ),
    ]
