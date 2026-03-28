from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import Person  # นำเข้าโมเดล Person

# Create your views here.
def index(request):
    # ดึงข้อมูลทั้งหมดจากโมเดล Person
    all_Person = Person.objects.all()
    
    # ส่งข้อมูลไปยัง template index.html ผ่านตัวแปร all_person
    return render(request, "index.html", {"all_person": all_Person})

def about(request):
    return render(request, "about.html")

def form(request):
    return render(request, "form.html")