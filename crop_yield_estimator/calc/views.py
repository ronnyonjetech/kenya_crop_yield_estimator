from django.shortcuts import render
from .models import Calculator
# Create your views here
def home(request):
    name={'name':'Ron'}
    calc=Calculator.objects.all()
    return render(request,'index.html',name)
def add(request):
    val1=int(request.POST['num1'])
    val2=int(request.POST['num2'])
    res=val1+val2
    return render(request,'results.html',{'result':res})
def predict(request):
    return render(request,'prediction.html')