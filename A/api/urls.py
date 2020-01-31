from django.urls import path
from .views import VacancyView, VacanciesView


urlpatterns = [
    path('vacancies/', VacanciesView.as_view()),
    path('vacancy/<uuid:vacancy_id>', VacancyView.as_view()),
]
