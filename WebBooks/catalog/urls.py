from django.urls import path
from .import views
from ..WebBooks.urls import urlpatterns

urlpatterns = [
    path('', views.index, name = "index"),
]