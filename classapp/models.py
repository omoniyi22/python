from django.db import models

from django.contrib.auth.models import User


class Teacher(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True, null=True, blank=True)

    specialization = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Course(models.Model):
    title = models.CharField(max_length=200)
    code = models.CharField(max_length=20, unique=True)
    teacher = models.ForeignKey(
        Teacher,
        on_delete=models.CASCADE,
        related_name="courses"
    )

    def __str__(self):
        return self.title


class Student(models.Model):
    user = models.OneToOneField(
        User, on_delete=models.CASCADE)  # <--- Add this
    courses = models.ManyToManyField(Course, related_name="students")
    enrolled_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.first_name} {self.user.last_name}"
