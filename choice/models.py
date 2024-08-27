from django.db import models

# Create your models here.
from django.db import models

class UserData(models.Model):
    BRANCH_CHOICES = [
        ('CE', 'Computer Engineering'),
        ('IT', 'Information Technology'),
        ('CSE', 'Computer Science Engineering'),
        ('CSD', 'Computer Science and Design'),
        ('AIML', 'Artificial Intelligence and Machine Learning'),
        ('AIDS', 'Artificial Intelligence and Data Science'),
        ('RAI', 'Robotics and AI'),
        ('CSIT', 'Computer Science and Information Technology'),
        ('CST', 'Computer Science and Technology'),
    ]

    EXAM_CHOICES = [
        ('GPSC', 'GPSC'),
        ('UPSC', 'UPSC'),
        ('GATE', 'GATE'),
        ('OTHER', 'Other Competitive Exam'),
    ]

    name = models.CharField(max_length=100)
    enrollment_no = models.CharField(max_length=50)
    branch = models.CharField(max_length=10, choices=BRANCH_CHOICES)
    contact_no = models.CharField(max_length=15)
    email = models.EmailField()
    choices = models.CharField(max_length=20, choices=EXAM_CHOICES)
    
    def __str__(self):
        return self.name
