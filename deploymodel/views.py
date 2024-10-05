from django.http import HttpResponse
from django.shortcuts import render
import joblib 



def home(request):
    return render(request,"home.html")

def result(request):
    
    cls=joblib.load("CRM.pkl")
    
    lis=[]
    
    lis.append(request.GET['Temparature'])
    lis.append(request.GET['Humidity '])
    lis.append(request.GET['Moisture '])
    lis.append(request.GET['Soil Type'])
    lis.append(request.GET['Crop Type'])
    lis.append(request.GET['Nitrogen'])
    lis.append(request.GET['Potassium '])
    lis.append(request.GET['Phosphorous '])
    print(lis)
    
    
    ans=cls.predict([lis])    
    
    
    return render(request,"result.html",{'ans':ans})