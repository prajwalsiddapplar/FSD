from django.shortcuts import render
from django.http import JsonResponse
from .models import Feedback

def home(request):
    data = Feedback.objects.all()
    return render(request, "feedback.html", {"data": data})

def add_feedback(request):
    if request.method == "POST":
        name = request.POST['name']
        msg = request.POST['message']
        Feedback.objects.create(name=name, message=msg)
        return JsonResponse({'name': name, 'message': msg})
