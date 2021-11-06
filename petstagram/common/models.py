from django.db import models

# Create your models here.
from pets.models import Pet


class Comment(models.Model):
    pet = models.ForeignKey(Pet, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self):
        return self.comment
