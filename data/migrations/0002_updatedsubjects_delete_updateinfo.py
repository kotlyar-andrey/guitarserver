# Generated by Django 4.0.5 on 2022-12-14 11:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('data', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='UpdatedSubjects',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('version', models.IntegerField(default=0, verbose_name='Версия данных')),
                ('edited_beats', models.ManyToManyField(to='data.beat', verbose_name='Измененнные бои')),
                ('edited_chords', models.ManyToManyField(blank=True, to='data.chord', verbose_name='Измененные аккорды')),
                ('edited_lessons', models.ManyToManyField(blank=True, to='data.lesson', verbose_name='Измененные уроки')),
            ],
            options={
                'verbose_name': 'Информация об обновлении',
                'verbose_name_plural': 'Информация об обновлении',
                'ordering': ('-version',),
            },
        ),
        migrations.DeleteModel(
            name='UpdateInfo',
        ),
    ]
