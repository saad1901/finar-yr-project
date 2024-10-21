from django.db import models
from django.contrib.auth.models import User

class S3File(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Link file to the user
    file = models.FileField(upload_to='files/')  # Store files in the S3 bucket
    file_name = models.CharField(max_length=255)
    file_size = models.IntegerField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs):
        # Automatically calculate the file size when saving
        if self.file:
            self.file_size = self.file.size
            self.file_name = self.file.name.split('/')[-1]  # Get the file name without the path
        super().save(*args, **kwargs)

    def __str__(self):
        return self.file_name

    class Meta:
        ordering = ['-uploaded_at']  # Order files by upload date (newest first)
