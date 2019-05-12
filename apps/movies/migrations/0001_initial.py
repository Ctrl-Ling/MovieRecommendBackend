# Generated by Django 2.0.5 on 2018-07-06 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movies',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(default='', help_text='电影名', max_length=30, verbose_name='电影名')),
                ('cover', models.CharField(default='', help_text='封面url', max_length=400, verbose_name='封面url')),
                ('director', models.CharField(default='', help_text='导演', max_length=20, verbose_name='导演')),
                ('actor', models.CharField(default='', help_text='主演', max_length=100, verbose_name='主演')),
                ('type', models.CharField(default='', help_text='类型', max_length=50, verbose_name='类型')),
                ('country', models.CharField(default='', help_text='国家/地区', max_length=50, verbose_name='国家/地区')),
                ('time', models.CharField(default='', help_text='片长', max_length=20, verbose_name='片长(分钟)')),
                ('grade', models.IntegerField(default=0, help_text='评分', max_length=10, verbose_name='评分')),
                ('desc', models.TextField(default='', help_text='剧情简介', max_length=1000, verbose_name='剧情简介')),
            ],
            options={
                'verbose_name': '电影详情',
                'verbose_name_plural': '电影详情',
            },
        ),
    ]
