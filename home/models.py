from django.db import models

class Video(models.Model):
    title = models.CharField(max_length=200)
    video = models.FileField(upload_to='videos/')
    upload = models.DateTimeField(auto_now_add=True)

    def __self__(self):
        return self.title
