from django.shortcuts import render
from .models import Calculator
import pickle
from django.contrib import messages
#global variable
items=[]
# Create your views here
def home(request):
    name={'name':'Ron'}
    calc=Calculator.objects.all()
    return render(request,'index.html',name)
# def add(request):
#     val1=int(request.POST['num1'])
#     val2=int(request.POST['num2'])
#     res=val1+val2
#     return render(request,'results.html',{'result':res})
def calculations(request):
  
  if request.method == 'POST':
      val11=int(request.POST['year'])
      val12=int(request.POST['rainfall'])
      val13=int(request.POST['pesticide'])
      val14=int(request.POST['temperature'])
      val15=request.POST['item']
      #Let's use switch statements to handle the items property
      match val15:
       case "cassava":
        items=[val11,val12,val13,val14]+[1,0,0,0,0,0,0,0,0]

       case "maize":
        items=[val11,val12,val13,val14]+[0,1,0,0,0,0,0,0,0]

       case "plantains":
        items=[val11,val12,val13,val14]+[0,0,1,0,0,0,0,0,0]
    
       case "potatoes":
        items=[val11,val12,val13,val14]+[0,0,0,1,0,0,0,0,0]

       case "rice":
        items=[val11,val12,val13,val14]+[0,0,0,0,1,0,0,0,0]
       
       case "sorghum":
        items=[val11,val12,val13,val14]+[0,0,0,0,0,1,0,0,0]

       case "soybeans":
        items=[val11,val12,val13,val14]+[0,0,0,0,0,0,1,0,0]

       case "sweet_potatoes":
        items=[val11,val12,val13,val14]+[0,0,0,0,0,0,0,1,0]

       case "wheat":
        items=[val11,val12,val13,val14]+[0,0,0,0,0,0,0,0,1]

       case _:
         print("Invalid inputs") 
  print(items) 
  #Lets load the deployed machine learning model
  with open('deployed_model/model','rb') as f:
    machineLearningModel=pickle.load(f)
    
  result=machineLearningModel.predict([items])
  
  messages.info(request,result)
  return render(request,'prediction.html',{'result':result})

def predict(request):
    
    return render(request,'prediction.html')