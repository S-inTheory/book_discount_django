from django.db import models


class Authors(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)


class Publisher(models.Model):
    name = models.CharField(max_length=100)


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    publisher = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    isbn = models.CharField(max_length=100, unique=True)
    cover = models.CharField(max_length=600)
    pages = models.CharField(max_length=4)
    chitai_gorod_price = models.CharField(max_length=4, null=True, default='нет в наличии')




