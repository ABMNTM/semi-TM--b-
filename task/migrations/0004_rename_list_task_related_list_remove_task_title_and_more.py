# Generated by Django 5.0.2 on 2024-03-17 08:37

import django.db.models.deletion
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('task', '0003_rename_date_for_delivery_task_due_date'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.RenameField(
            model_name='task',
            old_name='list',
            new_name='related_list',
        ),
        migrations.RemoveField(
            model_name='task',
            name='title',
        ),
        migrations.RemoveField(
            model_name='task',
            name='type',
        ),
        migrations.AddField(
            model_name='task',
            name='status',
            field=models.CharField(choices=[('TD', 'برای انجام'), ('DI', 'در حال انجام'), ('DN', 'انجام شده')], default='TD', max_length=2),
        ),
        migrations.AlterField(
            model_name='list',
            name='name',
            field=models.CharField(max_length=250),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('content', models.TextField()),
                ('date_created', models.DateTimeField(auto_now=True)),
                ('author', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to=settings.AUTH_USER_MODEL)),
                ('task', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='task.task')),
            ],
        ),
        migrations.DeleteModel(
            name='POV',
        ),
    ]
