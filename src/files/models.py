from django.db import models


# Create your models here.
class Upload(models.Model):
    fileName = models.CharField(max_length=255)
    info = models.TextField(max_length=100, blank=True)
    document = models.FileField(upload_to='files')
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return "%s" % self.fileName

    def delete(self, *args, **kwargs):
        self.document.delete()
        super().delete(*args, **kwargs)