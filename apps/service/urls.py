from django.urls import path

from . import views

urlpatterns = [
    path('get/', views.ServiceListView),
    path('post/', views.ServiceCreateView),


]
