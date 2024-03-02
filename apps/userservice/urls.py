from django.urls import path

from . import views

urlpatterns = [
    path('get/', views.UserListView.as_view()),
    path('post/', views.UserCreateView.as_view()),

]
