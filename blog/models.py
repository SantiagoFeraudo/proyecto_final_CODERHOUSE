from django.db import models
import datetime
from django.conf import settings

# Create your models here.


class Post(models.Model):
    title = models.CharField(max_length=1000)
    description = models.TextField()
    image = models.ImageField(upload_to="blog/images")
    date = models.DateField(datetime.date.today)


class Comment(models.Model):
    content = models.TextField(max_length=1000, help_text='Ingrese un comentario.')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True)
    post_date = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)

    class Meta:
        ordering = ['-post_date']

    def __str__(self):
        len_title = 15
        if len(self.content) > len_title:
            return self.content[:len_title] + '. . .'
        return self.content
    
