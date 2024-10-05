
from django.contrib import admin
from django.urls import path
from deploymodel import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home),
    path('result/',views.result,name="result")
]
