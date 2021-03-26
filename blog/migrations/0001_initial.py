# Generated by Django 3.1.7 on 2021-03-26 05:40

from django.db import migrations, models
import mdeditor.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AnimeModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.TextField(default='https://i.gzn.jp/img/2019/12/14/anime-2020winter/00.png')),
                ('title', models.CharField(max_length=30)),
                ('content', models.TextField()),
                ('hp', models.TextField(default='https://www.tus.ac.jp/')),
                ('infomation', models.TextField(default='特になし')),
                ('date', models.DateField(auto_now=True)),
                ('category', models.CharField(choices=[('Greate', 'イチオシ'), ('Now', '現在'), ('Old', '過去')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='BlogModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('content', mdeditor.fields.MDTextField()),
                ('postdate', models.DateField(auto_now_add=True)),
                ('editdate', models.DateField(auto_now=True)),
                ('category', models.CharField(choices=[('math', '数学'), ('program', 'プログラミング'), ('game', 'ゲーム'), ('sports', 'スポーツ'), ('anime', 'アニメ'), ('prime', '素数大富豪'), ('life', '日常'), ('other', 'その他')], max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='RamennModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('postdate', models.DateField(auto_now_add=True)),
                ('content', models.CharField(max_length=400)),
                ('picture', models.FileField(upload_to='static/img/Ramenn/')),
            ],
        ),
        migrations.CreateModel(
            name='SampleModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
