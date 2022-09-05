from django.urls import path

from main.views import show_home, show_profile, show_dashboard, show_pet_photo_details

urlpatterns = (
    path('', show_home, name='index'),
    path('dashboard/', show_dashboard, name='dashboard'),
    path('profile/', show_profile, name='profile'),
    path('photo/details/<int:pk>/', show_pet_photo_details, name='pet_photo_details'),
)
