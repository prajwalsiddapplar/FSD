
from django.shortcuts import render
from .forms import BiodataForm

def home(request):
    if request.method == "POST":
        form = BiodataForm(request.POST)
        if form.is_valid():
            return render(request,"result.html",{"data":form.cleaned_data})
    else:
        form = BiodataForm()

    return render(request,"form.html",{"form":form})

