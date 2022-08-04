from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=100)
    author = models.OneToOneField('Author', on_delete=models.CASCADE)
    year_published = models.CharField(max_length=10)
    review = models.PositiveIntegerField()
    category = models.ForeignKey('Category', on_delete=models.CASCADE)
    
    def __str__(self):
        return self.title 
    
    
    
class Author(models.Model):
    name = models.CharField(max_length=50)
    age = models.CharField(max_length=10)
        
    def __str__(self):
        return self.name
    
    
class Category(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name