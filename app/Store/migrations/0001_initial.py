# Generated by Django 3.2.13 on 2022-05-09 21:01

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='eBook',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=51)),
                ('price', models.FloatField()),
                ('img_url', models.CharField(max_length=2048)),
            ],
        ),
    ]
