from django.urls import path

from . import views

urlpatterns = [
    path('get/', views.OrderListView.as_view()),
    path('post/', views.OrderCreateView.as_view()),

]