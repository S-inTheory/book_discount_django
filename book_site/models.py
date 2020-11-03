from django.db import models


class LabirintAuthors(models.Model):
    full_name = models.CharField(max_length=100, unique=True)


class LabirintPublisher(models.Model):
    pubhouse = models.CharField(max_length=100)


class Labirint(models.Model):
    labirint_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(LabirintAuthors, on_delete=models.CASCADE)
    pubhouse = models.ForeignKey(LabirintPublisher, on_delete=models.CASCADE)
    cover = models.CharField(max_length=600)
    labirint_price = models.CharField(max_length=4, null=True, default='нет в наличии')
    labirint_link = models.CharField(max_length=200, null=True, default='#')


class Book24Authors(models.Model):
    full_name = models.CharField(max_length=100, unique=True)



