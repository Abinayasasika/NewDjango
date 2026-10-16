from django.shortcuts import render
from .models import Student,Students,Course,User

# Create your views here.
def home(request):
    student = Student(
        name="raju",
        age=23,
        email="raju@gmail.com",
        course="python",
        mark=85
    )
#     student.save()
    
#     Student.objects.create(
#         name="abi",
#         age=23,
#         email="abi@gmail.com",
#         course="python",
#         mark=85
#     )

#     return render(request, "home.html")

# #Without select Related:
# student = Students.objects.all()
# #print(student)

# for std in student:
#     print(std.name,std.Course.name)

# #With Select Related:
# Student = Students.objects.select_related("Course")
# print(Student)

# for std in Student:
#     print(std.name,std.Course.name)

# #without Prefetch_related():
# courses = Course.objects.prefetch_related("students")

# for course in courses:
#     for student in course.students.all():
#         print(course.name,student.name)

#User.objects.create(name = "Raj",age = 23)
#User.objects.filter(id = 1).update(name = "Kavin Kumar")
# user_date = User.objects.create(
#     name = "Naveen",
#     age = 20
# )

# user_date.name = "Naveen Kumar"
# user_date.save()

    

