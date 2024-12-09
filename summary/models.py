from django.db import models

from django.db import models

class UploadedFile(models.Model):
    name = models.CharField(max_length=255)
    uploaded_at = models.DateTimeField(auto_now_add=True)
    summary = models.TextField()

    def __str__(self):
        return self.name