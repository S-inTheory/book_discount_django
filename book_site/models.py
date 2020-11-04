from django.db import models


class LabirintAuthor(models.Model):
    full_name = models.CharField(max_length=100, unique=True)


class LabirintPublisher(models.Model):
    pubhouse = models.CharField(max_length=100)


class Labirint(models.Model):
    labirint_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(LabirintAuthor, on_delete=models.CASCADE)
    pubhouse = models.ForeignKey(LabirintPublisher, on_delete=models.CASCADE)
    cover = models.CharField(max_length=600)
    labirint_price = models.CharField(max_length=4, null=True, default='нет в наличии')
    labirint_link = models.CharField(max_length=200, null=True, default='#')


class Book24Author(models.Model):
    full_name = models.CharField(max_length=100, unique=True)


class Book24(models.Model):
    book24_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Book24Author, on_delete=models.CASCADE)
    cover = models.CharField(max_length=100)
    book24_price = models.CharField(max_length=5)
    book24_link = models.CharField(max_length=200)


class ChitaiGorodAuthor(models.Model):
    full_name = models.CharField(max_length=100, unique=True)


class ChitaiGorod(models.Model):
    chitaigorod_id = models.CharField(max_length=100, unique=True)
    title = models.CharField(max_length=100)
    author = models.ForeignKey(ChitaiGorodAuthor, on_delete=models.CASCADE)
    cover = models.CharField(max_length=100)
    chitaigorod_price = models.CharField(max_length=5)
    chitaigorod_link = models.CharField(max_length=200)

