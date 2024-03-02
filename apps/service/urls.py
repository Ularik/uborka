from django.urls import path

from . import views

urlpatterns = [
    path('get/', views.ServiceListView.as_view()),
    path('post/', views.ServiceCreateView.as_view()),


]
