from django.shortcuts import render
from .models import Student

def home(request):
    if request.method == "POST":
        usn = request.POST['usn']
        name = request.POST['name']
        sub = request.POST['subject']
        marks = request.POST['marks']

        Student.objects.create(
            usn=usn, name=name,
            subject_code=sub, cie_marks=marks
        )

    return render(request, "form.html")

def low(request):
    data = Student.objects.filter(cie_marks__lt=20)
    return render(request, "result.html", {"data": data})

