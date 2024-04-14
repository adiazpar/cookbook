from django.shortcuts import render, redirect
from django.http import HttpResponse, JsonResponse, HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import logout
from .models import Recipe

# Create your views here.
def home(request):
    return render(request, 'cookbook_app/home.html')

# ------------------------ RECIPE VIEWS ------------------------- #
# Creates the recipes page:
#@login_required(login_url='/login/')
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        Recipe.objects.create(
            name = name,
            description = description,
        )
        return redirect('/')

    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            day_icontains=request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request, 'cookbook_app/recipe.html', context)

# Updates the recipe's data:
#@login_required(login_url='/login/')
def update_recipe(request, id):
    queryset = Recipe.objects.get(id=id)

    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')

        queryset.name = name
        queryset.description = description
        queryset.save()
        return redirect('/')

    context = {'recipe': queryset}
    return render(request, 'cookbook_app/update_recipe.html', context)

# Deletes the recipe's data:
#@login_required(login_url='/login/')
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/')


# ------------------------- AUTH VIEWS -------------------------- #
# Login page for user:
def login_page(request):
    if request.method == 'POST':
        try:
            username = request.POST.get['username']
            password = request.POST.get['password']
            user_obj = User.objects.filter(username=username)
            if not user_obj.exists():
                messages.error(request, 'Username not found')
                return redirect('/login/')
            user_obj = authenticate(username=username, password=password)
            if user_obj:
                login(request, user_obj)
                return redirect('recipes')
            messages.error(request, 'Wrong Password')
            return redirect('/login/')

        except Exception as e:
            messages.error(request, 'Something went wrong...')
            return redirect('/register/')

    return render(request, "cookbook_app/login.html")

# Register page for user:
def register_page(request):
    if request.method == 'POST':
        try:
            username = request.POST.get['username']
            password = request.POST.get['password']
            user_obj = User.objects.filter(username=username)
            if user_obj.exists():
                messages.error(request, 'Username already exists')
                return redirect('/register/')
            user_obj = User.objects.create(username=username)
            user_obj.set_password(password)
            user_obj.save()
            messages.success(request, 'Account created successfully')
            return redirect('/login')

        except Exception as e:
            messages.error(request, 'Something went wrong...')
            return redirect('/register')

    return render(request, "cookbook_app/register.html")

# Logout functionality:
def custom_logout(request):
    logout(request)
    return redirect('login')