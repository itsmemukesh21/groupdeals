# Generated by Django 2.2.2 on 2019-06-06 05:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0004_auto_20190605_1320'),
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=100, null=True)),
                ('minimum_deposit', models.IntegerField(blank=True, null=True)),
                ('price', models.IntegerField(blank=True, null=True)),
                ('main_image', models.ImageField(blank=True, null=True, upload_to='')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
                ('descripition', models.TextField(blank=True, null=True)),
                ('bragets', models.CharField(blank=True, max_length=100, null=True)),
            ],
        ),
    ]