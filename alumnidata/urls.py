import imp
from django.urls import path
from alumnidata import views

urlpatterns = [
    path('', views.index, name="Homepage"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_new, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('user/<int:id>/', views.userpage, name='user'),
]