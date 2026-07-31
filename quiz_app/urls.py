from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('quiz/<str:category>/', views.index, name='index'),
    path('api/questions/<str:category>/', views.get_questions, name='get_questions'),
    path('login/', views.login_view, name='login'),
    path('register/', views.register_view, name='register'),
    path('logout/', views.logout_view, name='logout'),
    path('leaderboard/', views.leaderboard, name='leaderboard'),
    path('api/submit_score/<str:category>/', views.submit_score, name='submit_score'),
    path('profile/', views.profile, name='profile'),
]
