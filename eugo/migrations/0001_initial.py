# Generated by Django 4.0.2 on 2022-02-22 01:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Lecturer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('duration', models.SlugField(max_length=255, unique=True)),
                ('hp', models.TextField()),
                ('attack', models.DateTimeField(auto_now_add=True)),
                ('subject', models.TextField()),
                ('sprite', models.TextField()),
                ('pos', models.TextField()),
                ('lecID', models.TextField()),
            ],
        ),
    ]
