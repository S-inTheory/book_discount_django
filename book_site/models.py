from django.db import models


class Authors(models.Model):
    full_name = models.CharField(max_length=100)
    full_name_chitai_gorod = models.CharField(max_length=100, null=True)


class Publisher(models.Model):
    pubhouse = models.CharField(max_length=100)


class Books(models.Model):
    title = models.CharField(max_length=100)
    author = models.ForeignKey(Authors, on_delete=models.CASCADE)
    pubhouse = models.ForeignKey(Publisher, on_delete=models.CASCADE)
    cover = models.CharField(max_length=600)
    labirint_price = models.CharField(max_length=4, null=True, default='нет в наличии')
    labirint_link = models.CharField(max_length=200, null=True, default='#')




