import imp
from django.urls import path
from alumnidata import views

urlpatterns = [
    path('', views.index, name="Homepage"),
    path('signup/', views.signup, name='signup'),
    path('login/', views.login_new, name='login'),
    path('logout/', views.logout_request, name='logout'),
    path('user/<int:id>/', views.userpage, name='user'),
    path('fofs/<int:id>/', views.fieldstudy_page, name='fofs'),
    path('job/<int:id>/', views.job_page, name='updatejob'),
    path('education/<int:id>/', views.education_page, name='updateeducation'),
    path('achievement/<int:id>/', views.achievement_page, name='updateachievement'),
]