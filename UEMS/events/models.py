from django.db import models
from django.utils.text import slugify

# Create your models here.

from django.db import models

# Choices for event status
STATUS_CHOICES = [
    ('upcoming', 'Upcoming'),
    ('ongoing', 'Ongoing'),
    ('completed', 'Completed'),
]

# Predefined event categories
CATEGORY_CHOICES = [
    ('workshop', 'Workshop'),
    ('seminar', 'Seminar'),
    ('conference', 'Conference'),
    ('networking', 'Networking'),
    ('competition', 'Competition'),
    ('social', 'Social Event'),
    ('academic', 'Academic Talk'),
    ('sports', 'Sports Event'),
    ('career', 'Career Fair'),
    ('volunteer', 'Volunteering Event'),
    ('cultural', 'Cultural Festival'),
    ('club_meeting', 'Club Meeting'),
    ('research', 'Research Symposium'),
    ('hackathon', 'Hackathon'),
    ('orientation', 'Orientation Program'),
]

class Event(models.Model):
    name = models.CharField(max_length=255)
    poster = models.ImageField(default='fallback.png', blank=True)
    description = models.TextField()
    start_datetime = models.DateTimeField()
    end_datetime = models.DateTimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='upcoming')
    participation_limit = models.PositiveIntegerField()
    category = models.CharField(max_length=20, choices=CATEGORY_CHOICES)
    fees = models.PositiveIntegerField(default=0)
    slug = models.SlugField(unique=True, blank=True)

    def __str__(self):
        return self.name

    def save(self, *args, **kwargs):
        if not self.slug:  # Only generate slug if it is not already set
            self.slug = slugify(self.name)  
        super().save(*args, **kwargs)  # Call the original save() method

    def get_fees_display(self):
        return "Free" if self.fees == 0 else f"RM {self.fees}"