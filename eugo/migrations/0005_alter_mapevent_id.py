# Generated by Django 4.0.2 on 2022-03-01 18:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eugo', '0004_completeevents'),
    ]

    operations = [
        migrations.AlterField(
            model_name='mapevent',
            name='id',
            field=models.CharField(max_length=100, primary_key=True, serialize=False),
        ),
    ]
