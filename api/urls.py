from django.urls import path
from .views import TodoView


urlpatterns = [
    path('todos/', TodoView.as_view())
    
]
