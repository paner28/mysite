from django.db import models
from mdeditor.fields import MDTextField

class SampleModel(models.Model):
    title = models.CharField(max_length=100)
    number = models.IntegerField()

CATEGORY = (('math','数学'),('program','プログラミング'),('game','ゲーム'),('sports','スポーツ'),('anime','アニメ'),('prime','素数大富豪'),('life','日常'),('other','その他'))

ANIME_CATEGORY = (('Greate', 'イチオシ'),('Now', '現在'),('Old', '過去'))

class BlogModel(models.Model):
    title = models.CharField(max_length=100)
    content = MDTextField()
    postdate = models.DateField(auto_now_add=True)
    editdate = models.DateField(auto_now=True)
    category = models.CharField(
        max_length=50,
        choices = CATEGORY
    )
    def __str__(self):
        return self.title

class AnimeModel(models.Model):
    image = models.TextField(default='https://i.gzn.jp/img/2019/12/14/anime-2020winter/00.png')
    title = models.CharField(max_length=30)
    content = models.TextField()
    hp = models.TextField(default="https://www.tus.ac.jp/")
    infomation = models.TextField(default="特になし")
    date = models.DateField(auto_now=True)
    category = models.CharField(
        max_length=50,
        choices = ANIME_CATEGORY
    )
    def __str__(self):
        return self.title

class RamennModel(models.Model):
    title = models.TextField()
    postdate = models.DateField(auto_now_add=True)
    content = models.CharField(max_length=400)
    picture = models.FileField(upload_to='static/img/Ramenn/')
    def __str__(self):
        return self.title