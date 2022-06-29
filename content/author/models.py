from django.db import models

# Create your models here.
class Post(models.Model):
    writter = models.CharField(max_length=20)
    text = models.TextField()

    def __str__(self):
        return self.writter