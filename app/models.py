from django.db import models

# Create your models here.


class Music(models.Model):
    song = models.FileField(upload_to='documents/')
    album = models.ImageField(upload_to='album/', null=True)
    title = models.CharField(max_length=200, null=True)

    def __str__(self):
        return f'{self.title}'
