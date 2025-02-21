from django.db import models
from .validators import file_size
from django.contrib.auth.models import User # type: ignore


# Create your models here.
class Feature(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)


class Chart(models.Model):
    name = models.CharField(max_length=100)
    details = models.CharField(max_length=500)

class Video(models.Model):
    caption=models.CharField(max_length=10000)
    video=models.FileField(upload_to="Video/",validators=[file_size])
    def __str__(self):
        return self.caption

class MentorshipApplication(models.Model):
     field1 = models.CharField(max_length=100)
     field2 = models.TextField()
     field3 = models.IntegerField()
    # ... other fields
     def __str__(self):
        return self.field1
     

from django.contrib.auth.models import User
from django.db import models

class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="professional_profile")
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    contact_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    image = models.ImageField(upload_to='professionals/', null=True, blank=True)


from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensuring user is linked to appointment
    professional = models.ForeignKey('Professional', on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    reason = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Appointment with {self.professional.name} on {self.date} at {self.time}"

class ChatMessage(models.Model):
    content = models.TextField()
    username = models.CharField(max_length=100, default="Anonymous")
    timestamp = models.DateTimeField(auto_now_add=True)
    
    # Remove `room_id` completely if not needed
    # room = models.ForeignKey(ChatRoom, on_delete=models.CASCADE, null=True, blank=True)  # Remove this if unused

    def __str__(self):
        return f"{self.username}: {self.content[:50]}"

from django.db import models

class Video(models.Model):
    CATEGORY_CHOICES = [
        ('Anxiety', 'Anxiety'),
        ('Depression', 'Depression'),
        ('PTSD', 'Post-Traumatic Stress Disorder'),
    ]

    title = models.CharField(max_length=255, null=True, blank=True)  # Ensure it allows null values
    category = models.CharField(max_length=50, choices=CATEGORY_CHOICES, null=True, blank=True)
    video_file = models.FileField(upload_to="videos/", null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    caption = models.TextField(null=True, blank=True)

    def __str__(self):
        return self.title if self.title else "Untitled Video"
    

from django.db import models

class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=[('Fiction', 'Fiction'), ('Non-Fiction', 'Non-Fiction')])
    pdf_file = models.FileField(upload_to='books/')  # Save PDFs in /media/books/
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Article(models.Model):
    title = models.CharField(max_length=255)
    category = models.CharField(max_length=100, choices=[('Health', 'Health'), ('Technology', 'Technology')])
    summary = models.TextField()
    url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title


class Course(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    level = models.CharField(max_length=50, choices=[('Beginner', 'Beginner'), ('Intermediate', 'Intermediate'), ('Advanced', 'Advanced')])
    url = models.URLField()
    uploaded_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

from django.db import models
from django.contrib.auth.models import User  # Import the User model

class CompletedCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Add this line
    title = models.CharField(max_length=255)
    description = models.TextField()
    completion_percentage = models.IntegerField(default=0)

    def __str__(self):
        return f"{self.user.username} - {self.title}"  # Ensure user.username is used




class Achievement(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField()
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.name
class QuizResult(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    score = models.IntegerField()
    date_taken = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.score}"
class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    progress = models.IntegerField(default=0)


    def __str__(self):
        return self.title
from django.db import models
from django.contrib.auth.models import User

class Appointment(models.Model):
    STATUS_CHOICES = [
        ('Upcoming', 'Upcoming'),
        ('Completed', 'Completed'),
        ('Canceled', 'Canceled'),
    ]

    user = models.ForeignKey(User, on_delete=models.CASCADE)
    professional_name = models.CharField(max_length=255, default="Unknown Professional")
    date = models.DateField()
    time = models.TimeField()
    status = models.CharField(max_length=10, choices=STATUS_CHOICES, default='Upcoming')
    reason = models.TextField(null=True, blank=True)  # Add this if missing

    def __str__(self):
        return f"{self.user.username} - {self.professional_name} ({self.date})"

from django.db import models

class CompletedCourse(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(default="No description provided.")  # ✅ FIXED
    completion_percentage = models.IntegerField(default=100)


from django.shortcuts import render
from .models import Quiz
import json

def quiz_list(request):
    quiz_categories = Quiz.objects.all()

    quizzes_json = json.dumps([
        {
            "id": quiz.id,
            "title": quiz.title,
            "description": quiz.description,
            "progress": quiz.progress if hasattr(quiz, "progress") else 0,
            "category": quiz.category
        }
        for quiz in quiz_categories
    ])

    return render(request, "quizzes.html", {
        "quizzes_json": quizzes_json
    })
from django.db import models
from django.contrib.auth.models import User

class CompletedCourse(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)  # Ensure this field exists
    title = models.CharField(max_length=255)
    description = models.TextField()
    completion_percentage = models.IntegerField(default=100)

    def __str__(self):
        return f"{self.user.username} - {self.title}"
from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100)
    progress = models.IntegerField(default=0)  # User's progress in percentage

    def __str__(self):
        return self.title
from django.db import models

class Message(models.Model):
    sender = models.CharField(max_length=255, default="System")  # Add a default value
    text = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

from django.db import models
from django.contrib.auth.models import User

class AnonymousPrivateMessage(models.Model):
    sender = models.CharField(max_length=100, default="Anonymous")
    recipient = models.CharField(max_length=100)  # Will store 'Everyone' or a specific username
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.sender} to {self.recipient}: {self.content[:30]}"
class Professional(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name="professional_profile")
    name = models.CharField(max_length=255)
    specialty = models.CharField(max_length=255)
    contact_email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, unique=True)
    image = models.ImageField(upload_to='professionals/', null=True, blank=True)
    available_slots = models.JSONField(default=list)  # Add this if missing
    booked_slots = models.JSONField(default=list)  # Add this if missing

from django.db import models

class Quiz(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    category = models.CharField(max_length=100, default="General")  # ADD CATEGORY

class Question(models.Model):
    quiz = models.ForeignKey(Quiz, on_delete=models.CASCADE, related_name="questions")  # Ensure related_name exists
    text = models.CharField(max_length=500)
    options = models.JSONField()
    correct_answer = models.CharField(max_length=255)

    def __str__(self):
        return self.text

from django.db import models
from django.contrib.auth.models import User

class Message(models.Model):
    sender = models.ForeignKey(User, on_delete=models.CASCADE, related_name="sent_messages")  # ✅ Ensures ForeignKey
    receiver = models.ForeignKey(User, on_delete=models.CASCADE, related_name="received_messages")  # ✅ Ensures ForeignKey
    content = models.TextField()
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.sender} to {self.receiver}"

