from django.shortcuts import render
from django.conf import settings
from django.core.exceptions import FieldError

from rest_framework import status
from rest_framework.views import APIView, Request, Response
from rest_framework.pagination import PageNumberPagination

from .serializers import VacanciesSerializer
from .models import VacanciesDataBase

from uuid import UUID

DEFAULT_PAGE_LIMIT = settings.DEFAULT_PAGE_LIMIT

# Create your views here.


class VacanciesView(APIView):


    def __clear_page_in_request(self, request):
        
        params = request.query_params.dict()
        if 'page' in params: params.pop('page')
        return params


    def get(self, request):

        params = self.__clear_page_in_request(request)

        try:
            vacancies = VacanciesDataBase.objects.filter(**params)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST )

        paginator = PageNumberPagination()
        paginator.default_limit = DEFAULT_PAGE_LIMIT
        page = paginator.paginate_queryset(vacancies, request)

        serializer = VacanciesSerializer(vacancies, many = True)
        return Response(data = serializer.data)

    def post(self, request):

        serializer = VacanciesSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)

        return Response(status = status.HTTP_400_BAD_REQUEST)

class VacancyView(APIView):
    
     def get(self, request, vacancy_id: UUID):

        try:
            vacancy = VacanciesDataBase.objects.get(pk = vacancy_id)

        except VacanciesDataBase.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

        serializer = VacanciesSerializer(instance = vacancy)
        return Response(serializer.data)



     def delete(self, request, vacancy_id: UUID):

        try:
            vacancy = VacanciesDataBase.objects.get(pk = vacancy_id)

        except VacanciesDataBase.DoesNotExist:
            return Response(status.HTTP_404_NOT_FOUND)

        vacancy.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)

     def patch(self, request, vacancy_id: UUID):

        try:
            vacancy = VacanciesDataBase.objects.get(pk = vacancy_id)

        except ATE_Employees.DoesNotExist:
            return Response(status = status.HTTP_404_NOT_FOUND)

        serializer = VacanciesSerializer(instance = vacancy, data = request.data, partial = True)

        if serializer.is_valid():
            serializer.save()
            return Response(data = serializer.data, status = status.HTTP_202_ACCEPTED)

        return Response(data = serializer.errors, status = status.HTTP_400_BAD_REQUEST)