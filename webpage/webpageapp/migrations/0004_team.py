# Generated by Django 4.1.5 on 2023-02-26 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('webpageapp', '0003_rename_caken_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='Team',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=250)),
                ('image', models.ImageField(upload_to='pics')),
                ('descr', models.TextField()),
            ],
        ),
    ]
