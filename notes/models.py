from django.db import models

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

    def __str__(self):
        return self.title
