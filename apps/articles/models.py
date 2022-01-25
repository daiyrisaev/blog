from django.db import models


class ArticleCategory(models.Model):
    title=models.CharField(max_length=100,unique=True)


class Article(models.Model):
    title=models.CharField(max_length=120)
    short_description=models.TextField(max_length=600)
    is_active=models.PositiveIntegerField()
    category=models.ForeignKey(to=ArticleCategory,on_delete=models.CASCADE)


class ArticleTag(models.Model):

    pass