from django.urls import path
from . import views

urlpatterns = [
    path('normal_sort/', views.normal_sort),
    path('priority_queue/', views.priority_queue),
    path('bubble_sort/', views.bubble_sort),
    path('csv_to_DF/', views.csv_to_DF),
    path('missing_value/', views.missing_value),
    path('algorithm/', views.algorithm),
    path('jiwhan/', views.jiwhan),
    path('inwha/', views.inwha),
]

