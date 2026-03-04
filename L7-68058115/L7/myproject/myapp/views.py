from django.shortcuts import render

def contact(request):
    return render(request, "contact.html")

def form(request):
    return render(request, "form.html")