from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name="index"),
    path('delete/<int:id>/', views.delete_consume, name="delete"),
    path('chart-data/', views.chart_data, name="chart-data"),
    path('update-goals/', views.update_goals, name="update-goals"),
    path('add-food/', views.add_food, name="add-food"),
    path('register/', views.register, name="register"),
    path('login/', auth_views.LoginView.as_view(template_name="app/login.html"), name="login"),
    path('logout/', auth_views.LogoutView.as_view(), name="logout"),
]
