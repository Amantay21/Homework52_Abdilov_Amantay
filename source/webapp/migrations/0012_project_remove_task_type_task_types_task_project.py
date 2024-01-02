# Generated by Django 4.2.7 on 2023-12-27 14:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0011_alter_task_status_remove_task_type_task_type'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200, verbose_name='Название')),
                ('description', models.TextField(max_length=4000, verbose_name='Описание')),
                ('start_date', models.DateField(verbose_name='Дата начала')),
                ('end_date', models.DateField(blank=True, null=True, verbose_name='Дата конца')),
            ],
        ),
        migrations.RemoveField(
            model_name='task',
            name='type',
        ),
        migrations.AddField(
            model_name='task',
            name='types',
            field=models.ManyToManyField(related_name='tasks', to='webapp.type', verbose_name='Тип'),
        ),
        migrations.AddField(
            model_name='task',
            name='project',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.RESTRICT, related_name='tasks', to='webapp.project', verbose_name='Проект'),
            preserve_default=False,
        ),
    ]
