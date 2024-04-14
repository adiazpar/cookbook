from django.urls import path
from . import views
from django.contrib import admin

urlpatterns = [
    path('', views.home, name='home'),

    # Define URL pattern for the login view:
    path('login/', views.login_page, name='login'),
    path('logout/', views.custom_logout, name='logout'),
    path('register/', views.register_page, name='register'),
    path('admin/', admin.site.urls),

    path('recipes/', views.recipes, name='recipes'),
    path('update_recipe/<id>', views.update_recipe, name='update_recipe'),
    path('delete_recipe/<id>', views.delete_recipe, name='delete_recipe'),
]