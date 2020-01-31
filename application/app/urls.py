from django.urls import path
from .views import AppView


urlpatterns = [
    path('vacancies/', AppView.as_view()),
]
