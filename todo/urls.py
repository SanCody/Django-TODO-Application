from django.urls import path
from . import views

urlpatterns = [
    path('login/', views.login, name="login"),
    path('logout', views.logout, name="logout"),
    path('signup', views.signup, name="signup"),
    path('home/', views.home, name="home"),
    path('tasks/', views.task, name="tasks"),
    path('tasks/delete/<int:id>', views.delete, name='delete'),

]

