from django.db import models
from django.contrib.auth.models import User

CATEGORY_CHOICES = [
    ('Maths', 'Maths'),
    ('Physics', 'Physics'),
    ('Chemistry', 'Chemistry'),
    ('Biology', 'Biology'),
    ('Geography', 'Geography'),
    ('Aptitude', 'Aptitude'),
    ('Personality', 'Personality'),
    ('Current Affairs', 'Current Affairs'),
    ('Computer Science', 'Computer Science'),
    ('Space', 'Space'),
]

class Question(models.Model):
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Maths')
    text = models.CharField(max_length=255)

    def __str__(self):
        return f"[{self.category}] {self.text}"

class Option(models.Model):
    question = models.ForeignKey(Question, related_name='options', on_delete=models.CASCADE)
    text = models.CharField(max_length=255)
    is_correct = models.BooleanField(default=False)

    def __str__(self):
        return f"{self.text} ({'Correct' if self.is_correct else 'Incorrect'})"

class Score(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, default='Maths')
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.category}: {self.score}"

class UserProfile(models.Model):
    GENDER_CHOICES = [
        ('M', 'Male'),
        ('F', 'Female'),
        ('O', 'Other'),
        ('P', 'Prefer not to say')
    ]

    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='profile')
    age = models.IntegerField(null=True, blank=True)
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES, blank=True)
    bio = models.TextField(max_length=500, blank=True)
    about = models.TextField(max_length=1000, blank=True)
    profile_picture = models.ImageField(upload_to='profile_pics/', blank=True, null=True)

    def __str__(self):
        return f"{self.user.username}'s Profile"
