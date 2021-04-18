from django.urls import path

from .views import ListTodo, DetailTodo
from .views import UserRecordView

urlpatterns = [
    path('', ListTodo.as_view()),
    path('<int:pk>/', DetailTodo.as_view()),
    path('user/', UserRecordView.as_view(), name='users'),
]
