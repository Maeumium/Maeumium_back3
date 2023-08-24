from django.db import models

from django.db import models

class Diary(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    emotion = models.CharField(max_length=20)
    privacy = models.CharField(max_length=10)
    thumbnail = models.ImageField(upload_to='diary_thumbnails/')

    def __str__(self):
        return self.title
