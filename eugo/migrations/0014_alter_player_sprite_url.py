# Generated by Django 4.0.2 on 2022-02-27 15:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('eugo', '0013_remove_player_password_remove_player_salt_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='player',
            name='sprite_url',
            field=models.CharField(default='eugo\\static\\eugo\\img\teacher_sprites\teacher_1.png', max_length=100, null=True),
        ),
    ]
