from django.db import models

class Author(models.Model):
    first_name = models.CharField(max_length=60)
    last_name = models.CharField(max_length=60)

    def __str__(self):
        return f'{self.first_name} {self.last_name}'

class Book(models.Model):
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    title = models.CharField(max_length=255)
    genre = models.CharField(max_length=80)
    

    def __str__(self):
        return f'{self.title} by {self.author}'




