from django.urls import path

from . import views

urlpatterns = [
    path('get/', views.OrderListView),
    path('post/', views.OrderCreateView),

]