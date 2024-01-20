from django.urls import path
from .views import generate_image

app_name = 'generator'

urlpatterns = [
    path('', generate_image, name='generate_image'),
]
