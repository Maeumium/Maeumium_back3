from django.db import models

class Diary(models.Model):
    PRIVACY_CHOICES = (
        ('PUBLIC', '공개'),
        ('PRIVATE', '비밀')
    )
    
    EMOTION_CHOICES = (
        ('JOY', '기쁨'),
        ('EXCITEMENT', '설렘'),
        ('SAD', '슬픔'),
        ('ANGRY', '분노'),
        ('LONELY', '외로움')
    )
    
    privacy = models.CharField(max_length=10, choices=PRIVACY_CHOICES, default='PRIVATE')
    emotion = models.CharField(max_length=20, choices=EMOTION_CHOICES, default='JOY')
    title = models.CharField(max_length=200, null=True, blank=True)
    content = models.TextField()
    thumbnail = models.ImageField(upload_to='diary_thumbnails/', null=True, blank=True)

def __str__(self):
        return self.title