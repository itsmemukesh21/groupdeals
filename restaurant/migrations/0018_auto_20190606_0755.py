# Generated by Django 2.2.2 on 2019-06-06 07:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0017_auto_20190606_0754'),
    ]

    operations = [
        migrations.AlterField(
            model_name='products',
            name='created',
            field=models.DateField(auto_now_add=True, null=True),
        ),
    ]
