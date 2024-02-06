from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import * 
from django.contrib.auth.models import User
from django.contrib import messages
import os 

# Create your views here.
def receipes(request):
    print('Hello..\n')
    if request.method=="POST":
     data=request.POST 
     reciepe_image=data.get('reciepe_image')
     reciepe_name=data.get('reciepe_name')
     reciepe_description=data.get('reciepe_description')
     print(reciepe_name,reciepe_description)
     print(reciepe_image)
     Recipe.objects.create(
        recipe_image=reciepe_image,
        recipe_name=reciepe_name,
        recipe_description=reciepe_description

     )
     
     
    queryset=Recipe.objects.all()
    context={'recipes':queryset}
    return render(request,'recipes.html',context)

def delete_recipe(request,id):
   queryset=Recipe.objects.filter(id=id)
   queryset.delete()
   return redirect('/home/')

def update_recipe(request,id):
   queryset=Recipe.objects.get(id=id)
   
   if request.method == 'POST':
      data=request.POST
      reciepe_image=request.FILES.get('reciepe_image')
      reciepe_name=data.get('reciepe_name')
      reciepe_description=data.get('reciepe_description')
      queryset.recipe_name=reciepe_name
      queryset.recipe_description=reciepe_description
      queryset.recipe_image=reciepe_image

      queryset.save()
   context={'recipes':queryset}
   return render(request, 'update_recipe.html',context)
def search_results(request):
   if request.method=='GET':
       print('Your request is:\n')
       print(request.GET.get('search'))
       res=request.GET.get('search')
       if res:
        queryset=Recipe.objects.filter(recipe_name__icontains=request.GET.get('search'))
        if queryset is not None:
           print(queryset)
         #  print(queryset.recipe_name)
         #  print(queryset.recipe_description)
        else:
           print('No such query found')
        return HttpResponse('Doubt found')
       else:
         return HttpResponse('No Doubt found')
       
def login_page(request):
   return render(request,'login.html')

def register_page(request):
   if request.method=='POST':
      first_name=request.POST.get('first_name')
      last_name=request.POST.get('last_name')
      username=request.POST.get('username')
      password=request.POST.get('password') 
      user=User.objects.filter(username=username)
      if user.exists():
         messages.info(request,'Username already registered')
         return redirect('/register/')
      user=User.objects.create(
         first_name=first_name,
         last_name=last_name,
         username=username,
         
      )
      user.set_password(password)
      user.save()
      messages.info(request,'Registration successful')
   return render(request,'register.html')
