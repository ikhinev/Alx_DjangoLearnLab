from django.db import models
from django.conf import settings

class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
        related_name="books"
    )
    published_date = models.DateField()

    class Meta:
        permissions = [
            ("can_create", "Can create book"),
            ("can_delete", "Can delete book"),
        ]

    def __str__(self):
        return self.title
