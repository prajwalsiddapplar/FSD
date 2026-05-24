
from django.shortcuts import render
import html

# vulnerable
def home(request):
    name = request.POST.get('name','')
    return render(request,'home.html',{'name':name})

# secure
def secure(request):
    name = request.POST.get('name','')
    name = html.escape(name)   # prevent XSS
    return render(request,'secure.html',{'name':name})