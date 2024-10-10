
from django.urls import path
from home.views import home, dynamic_path

urlpatterns = [
    path('', home),
    path('dynamic_path/<int:num>/', dynamic_path)
]
