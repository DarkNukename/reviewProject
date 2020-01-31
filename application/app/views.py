from django.shortcuts import render
from django.conf import settings
from django.core.exceptions import FieldError

from rest_framework import status
from rest_framework.views import APIView, Request, Response
from rest_framework.pagination import PageNumberPagination

from .serializers import AppSerializer
from .models import AppDataBase

from uuid import UUID

DEFAULT_PAGE_LIMIT = settings.DEFAULT_PAGE_LIMIT


class AppView(APIView):


    def __clear_page_in_request(self, request):
        
        params = request.query_params.dict()
        if 'page' in params: params.pop('page')
        return params


    def get(self, request):

        params = self.__clear_page_in_request(request)

        try:
            vacancies = AppDataBase.objects.filter(**params)
        except:
            return Response(status = status.HTTP_400_BAD_REQUEST )

        paginator = PageNumberPagination()
        paginator.default_limit = DEFAULT_PAGE_LIMIT
        page = paginator.paginate_queryset(vacancies, request)

        serializer = AppSerializer(vacancies, many = True)
        return Response(data = serializer.data)
    
    def post(self, request):

        serializer = AppSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(status = status.HTTP_201_CREATED)

        return Response(status = status.HTTP_400_BAD_REQUEST)
