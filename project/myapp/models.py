from django.db import models
from datetime import date

# Create your models here.

class Widget(models.Model):
    name = models.CharField(max_length=140)
    font_size=models.IntegerField()
    price=models.IntegerField(default=True)
    quantity=models.IntegerField(default=True)
    total_price=models.IntegerField(default=True)

    
class MyUser(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    age = models.IntegerField()
    city = models.CharField(max_length=255)

    def __str__(self):
        return f"{self.first_name}"


class Blog(models.Model):
    name = models.CharField(max_length=100)
    tagline = models.TextField()

    def __str__(self):
        return self.name

class Author(models.Model):
    name = models.CharField(max_length=200)
    email = models.EmailField()

    def __str__(self):
        return self.name

class Entry(models.Model):
    blog = models.ForeignKey(Blog, on_delete=models.CASCADE)
    authors = models.ManyToManyField(Author)
    headline = models.CharField(max_length=255)
    body_text = models.TextField()
    pub_date = models.DateField()
    mod_date = models.DateField(default=date.today)
    number_of_comments = models.IntegerField(default=0)
    number_of_pingbacks = models.IntegerField(default=0)
    rating = models.IntegerField(default=5)

    def __str__(self):
        return self.headline

    def get_authors(self):
        return "\n".join([p.name for p in self.authors.all()])

   
class Dog(models.Model):
    name = models.CharField(max_length=200)
    data = models.JSONField(null=True)

    def __str__(self):
        return self.name

    