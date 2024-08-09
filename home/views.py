from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import logout, authenticate, login


# password for test user is 123456@Up
# Create your views here.
def index(request):
  print(request.user)
  if request.user.is_anonymous:
    return redirect("/login")
  return render(request, 'index.html')
  

def loginUser(request):
  if request.method=="POST":
    username = request.POST.get('username')
    password = request.POST.get('password')
    print(username, password)
    
    #Check for credentials i.e correct id and password
    user = authenticate(username=username, password=password)

    if user is not None:
    # A backend authenticated the credentials
      login(request, user)
      return redirect("/")
    
    else:
      #No backend authenticated the creadentials
      return render(request, 'login.html')
  
  return render(request, 'login.html')

def logoutUser(request):
  logout(request)
  return redirect("/login")