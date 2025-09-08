from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    published_date = models.DateField(null=True, blank=True)

    def __str__(self):
        return self.title
