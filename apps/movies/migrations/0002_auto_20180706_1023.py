# Generated by Django 2.0.5 on 2018-07-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movies',
            name='grade',
            field=models.IntegerField(default=0, help_text='评分', verbose_name='评分'),
        ),
    ]
