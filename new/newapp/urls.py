from django.urls import path
from . import views

urlpatterns = [
    path("hello_world/", views.hello_world ),
    path("class/", views.HelloWorld.as_view())
    
]
