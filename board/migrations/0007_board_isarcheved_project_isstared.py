# Generated by Django 5.0.3 on 2024-04-25 08:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('board', '0006_remove_board_description_remove_project_description_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='board',
            name='isArcheved',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='project',
            name='isStared',
            field=models.BooleanField(default=False),
        ),
    ]
