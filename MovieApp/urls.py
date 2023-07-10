from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name=""),
    path('register/', views.register, name="register"),
    path('login', views.login, name="login"),
    path('dashboard', views.dashboard, name="dashboard"),
    path('user-logout', views.user_logout, name="user_logout"),
    path('create-record', views.create_record, name="create-record"),
    path('movie-detail/<int:id>', views.movie_detail, name="movie-detail"),
    path("delete_record/<int:pk>", views.delete_record, name="delete_record"),
    path('update-record/<int:pk>', views.update_record, name="update-record"),
    path('download_dataset/', views.download_dataset, name="download_dataset"),
    
]



