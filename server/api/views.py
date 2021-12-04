# from django.db.models.query_utils import Q
# from django.shortcuts import render
# from django.db.models import query
# from django.http import request
from rest_framework import generics, views
from rest_framework.response import Response
from rest_framework.permissions import AllowAny, IsAuthenticated
from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import status
from rest_framework.fields import CurrentUserDefault
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
            return Response(data, status=status.HTTP_200_OK)
        except Exception:
            return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)


# class GetUserDataView(generics.RetrieveAPIView):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#     permission_classes = [AllowAny]


# class GetProjectsView(generics.ListAPIView):
#     queryset = Project.objects.all()
#     serializer_class = ProjectSerializer
#     permission_classes = [AllowAny]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['status', 'id', ]
#     search_fields = ['name', 'description']


# class GetRolesView(generics.ListAPIView):
#     queryset = Role.objects.all()
#     serializer_class = RoleSerializer
#     permission_classes = [AllowAny]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = []
#     search_fields = ['name',]


# class GetEmployeesView(generics.ListAPIView):
#     serializer_class = EmployeeSerializer
#     permission_classes = [AllowAny]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['id',]
#     search_fields = ['first_name', 'last_name', 'company_role']

#     def get_queryset(self):
#         queryset = Employee.objects.all()
#         skill = self.request.query_params.get('skill')
#         level = self.request.query_params.get('level')
    
#         if skill is not None and level is not None:
#             skill = Skill.objects.get(pk=skill)
#             level = int(level)
#             updated_qs = []
#             for emp in queryset:
#                 for l in emp.levels.all():
#                     if (l.skill == skill) and (l.level >= level):
#                         updated_qs.append(emp)
#             return list_to_queryset(Employee, updated_qs)
#         return queryset


# class GetAlmostFreeEmployeesView(generics.ListAPIView):
#     serializer_class = EmployeeSerializer
#     permission_classes = [AllowAny]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['id',]
#     search_fields = ['first_name', 'last_name', 'company_role']

#     def get_queryset(self):
#         queryset = Employee.objects.all()
#         startdate = date.today()
#         enddate = startdate + timedelta(days=14)
#         new_q = []
#         for elem in queryset:
#             for i in elem.get_projects:
#                 if i.end_date <= enddate:
#                     new_q.append(elem)
#         queryset = list_to_queryset(Employee, new_q)
#         skill = self.request.query_params.get('skill')
#         level = self.request.query_params.get('level')
    
#         if skill is not None and level is not None:
#             skill = Skill.objects.get(pk=skill)
#             level = int(level)
#             updated_qs = []
#             for emp in queryset:
#                 for l in emp.levels.all():
#                     if (l.skill == skill) and (l.level >= level):
#                         updated_qs.append(emp)
#             return list_to_queryset(Employee, updated_qs)
#         return queryset


# class GetLevelsView(generics.ListAPIView):
#     queryset = Level.objects.all()
#     serializer_class = LevelSerializer
#     permission_classes = [AllowAny]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = ['skill']
#     search_fields = []


# class GetSkillsView(generics.ListAPIView):
#     queryset = Skill.objects.all()
#     serializer_class = SkillSerializer
#     permission_classes = [AllowAny]
#     filter_backends = [DjangoFilterBackend, filters.SearchFilter, filters.OrderingFilter]
#     filterset_fields = []
#     search_fields = ['name', ]

