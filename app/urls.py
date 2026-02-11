from django.urls import path
from . import views

urlpatterns = [
    path('api/content',views.content_list, name='content_list'),
    path('api/content/<int:pk>',views.content_detail, name='content_detail'),
]