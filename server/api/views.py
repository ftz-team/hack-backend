# from django.db.models.query_utils import Q
# from django.shortcuts import render
# from django.db.models import query
# from django.http import request
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework import filters

from core.models import *
from .serializers import *


class GetEventsView(generics.ListAPIView):
    queryset = Event.objects.all()
    serializer_class = EventSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    search_fields = ['name', 'description']


class GetUserDataView(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            data = UserSerializer(request.user).data
            data['image'] = 'http://188.93.211.127:8000' + data['image']
            return Response(data, status=status.HTTP_200_OK)
        except Exception: 
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class GetEventContractExView(views.APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            data = 'http://188.93.211.127:8000' + EventSerializer(Event.objects.get(pk=request.GET['id'])).data['contract_example']
            return Response({'contract_ex': data}, status=status.HTTP_200_OK)
        except Exception: 
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


class UpdateUserDataView(generics.UpdateAPIView):
    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class GetApplicationsView(generics.ListAPIView):
    queryset = Application.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['event', 'user', ]


class CreateApplicationView(generics.CreateAPIView):
    queryset = Application.objects.all()
    serializer_class = CreateApplicationSerializer
    permission_classes = [AllowAny]


class GetStage1View(generics.ListAPIView):
    queryset = Stage1.objects.all()
    serializer_class = Stage1Serializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['application', 'status']


class GetStage2View(generics.ListAPIView):
    queryset = Stage2.objects.all()
    serializer_class = Stage2Serializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['application', 'status']


class GetStage3View(generics.ListAPIView):
    queryset = Stage3.objects.all()
    serializer_class = Stage3Serializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['application', 'status']


class GetStage4View(generics.ListAPIView):
    queryset = Stage4.objects.all()
    serializer_class = Stage4Serializer
    permission_classes = [AllowAny]
    filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
    filterset_fields = ['application', 'status']

#/////////////////////////////////////////////////////

class CreateStage1View(generics.UpdateAPIView):
    queryset = Stage1.objects.all()
    serializer_class = Stage1Serializer
    permission_classes = [AllowAny]


class CreateStage2View(generics.UpdateAPIView):
    queryset = Stage2.objects.all()
    serializer_class = Stage2Serializer
    permission_classes = [AllowAny]


class CreateStage3View(generics.UpdateAPIView):
    queryset = Stage3.objects.all()
    serializer_class = Stage3Serializer
    permission_classes = [AllowAny]


class CreateStage4View(generics.UpdateAPIView):
    queryset = Stage4.objects.all()
    serializer_class = Stage4Serializer
    permission_classes = [AllowAny]