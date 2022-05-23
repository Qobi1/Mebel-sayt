from django.db import models

# Create your models here.


class Category(models.Model):
    content = models.CharField(max_length=56)
    image_1 = models.ImageField(upload_to='api/images/')
    image_2 = models.ImageField(upload_to='api/images/')

    def __str__(self):
        return self.content


class Product(models.Model):
    type = models.CharField(max_length=56)
    name = models.CharField(max_length=56)
    image = models.ImageField()
    ctg = models.ForeignKey(Category, on_delete=models.CASCADE)
    price = models.IntegerField()
    g_length = models.IntegerField()
    g_width = models.IntegerField()
    g_height = models.IntegerField()
    s_length = models.IntegerField()
    s_width = models.IntegerField()
    s_height = models.IntegerField()
    guarantee = models.TextField()

    def __str__(self):
        return self.name