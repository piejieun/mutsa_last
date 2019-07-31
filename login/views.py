from django.shortcuts import render

# Create your views here.

def login(request):
    return render(request, 'login.html')

def result(request):
    Name=request.GET['name']
    Id=request.GET['id']
    Pass=request.GET['password']
    XY=request.GET['sex']
    Age=request.GET['age']
    AR=request.GET['address']
    return render(request, 'result.html',{'name':Name,'id':Id,'password':Pass,'sex':XY,'age':Age,'address':AR})