from django.http import HttpResponse
from django.shortcuts import render
import joblib 

import os

def home(request):
    return render(request,"home.html")

def result(request):
    model_path = os.path.join('static', 'CRM.pkl')
    joblib.dump(cls, 'CRM.pkl', compress=3)

    cls = joblib.load(model_path)
# def result():
#     model_path = os.path.join('static', 'CRM.pkl')
#     try:
#         return joblib.load(model_path)
#     except Exception as e:
#         print(f"Error loading model: {e}")
#         return None

# # Preload the model
# model = result()

    
    lis = []
    
    lis.append(request.GET['Temparature'])
    lis.append(request.GET['Humidity '])
    lis.append(request.GET['Moisture '])
    lis.append(request.GET['Soil Type'])
    lis.append(request.GET['Crop Type'])
    lis.append(request.GET['Nitrogen'])
    lis.append(request.GET['Potassium '])
    lis.append(request.GET['Phosphorous '])
    print(lis)
    
    ans = cls.predict([lis])    
    
    return render(request,"result.html",{'ans':ans})