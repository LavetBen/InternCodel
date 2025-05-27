from django.urls import path
from . import views

urlpatterns = [
    path('lectures/', views.list_lectures, name='list_lectures'),
    path('lectures/create/', views.create_lecture, name='create_lecture'),
    path('lectures/update/<int:pk>/', views.update_lecture, name='update_lecture'),
    path('lectures/delete/<int:pk>/', views.delete_lecture, name='delete_lecture'),
    path('upcoming/',views.upcoming_reminders,name='upcoming_reminders')
]
