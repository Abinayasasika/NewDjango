from django.db import models

# Create your models here.

class Student(models.Model):
    name=models.CharField(max_length=100)
    age=models.IntegerField()
    email=models.EmailField()
    course=models.CharField(max_length=100)
    mark=models.IntegerField()

    def __str__(self):
        return self.name

class Employee(models.Model):
    emp_id = models.CharField(max_length=20,unique=True)
    name = models.CharField(max_length=100)
    department = models.CharField(max_length=50)
    salary = models.IntegerField()
    joining_date = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.emp_id} - {self.name}"

class Course(models.Model):
    name = models.CharField(max_length=100)
    def __str__(self):
        return self.name

class Students(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()
    Course = models.ForeignKey(
        Course,
        on_delete=models.CASCADE,
        related_name="students"
    )

    def __str__(self):
        return self.name

class User(models.Model):
    name = models.CharField(max_length=100)
    age = models.IntegerField()

    def __str__(self):
        return self.name