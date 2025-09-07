from django.urls import path
from . import views
urlpatterns = [
    path('', views.home, name='home'),
    path('today/', views.todayTask, name='today'),
    path('pending/', views.pendingTask, name='pending'),
    path('overdue/', views.overdueTask, name='overdue'),
    path('createTask',views.createTask, name='add-task'),
    path('edit/<str:pk>', views.editTask, name='edit-task'),
    path('delete/<str:pk>/', views.deleteTask, name='delete-task'),
    path('completed/', views.completedTask, name='completed'),
    # path('task/<str:pk>/toggle/', views.toggle_completed, name='toggle_completed'),

]
