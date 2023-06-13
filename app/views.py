from django.shortcuts import render

# Create your views here.
def home_page(request):
    return render(request,'home_page.html')
def registration_page(request):
    return render(request,'registration_page.html')
def login_page(request):
    return render(request,'login_page.html')