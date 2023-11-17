from django.urls import path 
from .views import List ,Create

urlpatterns = [
    path('' , List.as_view(), name = "list"),
    path("create/" , Create.as_view() , name = "create"),
]