from django.urls import path
from .views import SendTaskView

urlpatterns = [
    path('send-task/', SendTaskView.as_view(), name='send-task'),
]
