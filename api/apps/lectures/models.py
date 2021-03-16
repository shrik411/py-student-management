from django.db import models
from apps.utils.models import AbstractTableMeta

# Create your models here.

class Lecture(AbstractTableMeta, models.Model):

    LEVEL = (
        (1, 'Level 1'),
        (2, 'Level 2')
    )

    title = models.CharField(max_length=100)
    description = models.TextField()
    lecture_name = models.CharField(max_length=100, default='',
                                    blank=True)

    
    date = models.DateField()
    duration = models.IntegerField(help_text='Enter number of hours')
    slides_url = models.CharField(max_length=255)
    level = models.IntegerField(choices=LEVEL, default=1)
    required = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.title}'