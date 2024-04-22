from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import CreateUserForm
from .models import Recipe

# Create your views here.
def home(request):
    return render(request, 'cookbook_app/home.html')

# ------------------------- AUTH VIEWS -------------------------- #
# Login page for user:
def login_page(request):
    if request.method == 'POST':
        try:
            username = request.POST.get('username')
            password = request.POST.get('password')

            # Check to see if the username exists in the database:
            user = User.objects.filter(username=username.lower())
            if not user.exists():
                messages.error(request, 'Username not found')
                return redirect('login')

            # Check to see if the username and password matches a user in the database:
            user = authenticate(request, username=username.lower(), password=password)
            if user is not None:
                login(request, user)
                return redirect('home')

            # If user isn't authenticated above, display wrong password:
            messages.error(request, 'Wrong Password')
            return redirect('login')

        except Exception as e:
            # Something went terribly wrong...
            messages.error(request, 'Something went wrong...')
            return redirect('register')

    return render(request, "cookbook_app/login.html")


# Register page for user:
def register_page(request):
    form = CreateUserForm()

    if request.method == 'POST':
        form = CreateUserForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('login')

    context = {'registerform':form}
    return render(request, "cookbook_app/register.html", context=context)

    """
    if request.method == 'POST':
        try:
            username = request.POST.get['username']
            email = request.POST.get['email']
            password = request.POST.get['password']
            user_obj = User.objects.filter(username=username.lower())

            if user_obj.exists():
                messages.error(request, 'Username already exists')
                return redirect('/register/')

            user_obj = User.objects.create(username=username.lower())
            user_obj.set_password(password)
            user_obj.set_email(email)
            user_obj.save()

            messages.success(request, 'Account created successfully')
            return redirect('/login')

        except Exception as e:
            messages.error(request, 'Something went wrong...')
            return redirect('/register')

    return render(request, "cookbook_app/register.html")
    """

# Logout functionality:
def custom_logout(request):
    logout(request)
    return redirect('login')


# ------------------------ RECIPE VIEWS ------------------------- #
# Creates the recipes page:
@login_required(login_url='/login/')
def recipes(request):
    if request.method == 'POST':
        data = request.POST
        name = data.get('name')
        description = data.get('description')
        Recipe.objects.create(
            name = name,
            description = description,
        )
        return redirect('/recipes')

    queryset = Recipe.objects.all()
    if request.GET.get('search'):
        queryset = queryset.filter(
            day_icontains=request.GET.get('search'))

    context = {'recipes': queryset}
    return render(request, 'cookbook_app/recipe.html', context)

# Updates the recipe's data:
@login_required(login_url='/login/')
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
@login_required(login_url='/login/')
def delete_recipe(request, id):
    queryset = Recipe.objects.get(id=id)
    queryset.delete()
    return redirect('/recipes')

