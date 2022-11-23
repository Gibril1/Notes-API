from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Notes(models.Model):
    CATEGORY_CHOICES = (
        ('H', 'Health'),
        ('S', 'Sports'),
        ('E', 'Entertainment'),
        ('P', 'Politics')
    )
    category = models.CharField(max_length=1, choices=CATEGORY_CHOICES)
    title = models.CharField(max_length=20)
    content = models.TextField()
    student = models.ForeignKey(User, on_delete=models.CASCADE, null=True)
    


    def __str__(self):
        return self.title
