from django.shortcuts import render
from .utils import get_random_students
import random

def main_page_view(request):
    students = get_random_students()
    random_student = random.choice(students)
    return render(request, 'students/main_page.html', {'student': random_student})

def students_page_view(request):
    students = get_random_students()
    return render(request, 'students/students_page.html', {'students': students})
