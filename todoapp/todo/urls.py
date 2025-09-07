from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('today/', views.today, name='today'),
    path('pending/', views.pending, name='pending'),
    path('overdue/', views.overude, name='overdue'),
    path('createTask',views.createTask, name='add-task'),
    path('edit/<str:pk>', views.editTask, name='edit-task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete')
]
