# Generated by Django 4.1.4 on 2022-12-27 12:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='layanan',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('platfrom', models.CharField(max_length=50)),
                ('berupa', models.CharField(max_length=50)),
            ],
        ),
    ]
