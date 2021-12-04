# from django.db.models.query_utils import Q
# from django.shortcuts import render
# from django.db.models import query
# from django.http import request
# from rest_framework import generics, views
# from rest_framework.response import Response
# from rest_framework.permissions import AllowAny, IsAuthenticated
# from django_filters.rest_framework import DjangoFilterBackend
# from rest_framework import status
# from rest_framework import filters
# from datetime import date, timedelta

from core.models import *
from .serializers import *


# def list_to_queryset(model, data):
#     from django.db.models.base import ModelBase

#     if not isinstance(model, ModelBase):
#         raise ValueError(
#             "%s must be Model" % model
#         )
#     if not isinstance(data, list):
#         raise ValueError(
#             "%s must be List Object" % data
#         )

#     pk_list = [obj.pk for obj in data]
#     return model.objects.filter(pk__in=pk_list)


# class CreateProjectView(generics.CreateAPIView):
#     queryset = Project.objects.all()
#     serializer_class = CreateProjectSerializer
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


# class AddMember(views.APIView):
#     permission_classes = [AllowAny]
#     def post(self, request):
#         try:
#             employee = Employee.objects.get(pk=request.data['employee_id'])
#             role = Role.objects.get(pk=request.data['role_id'])
#             project = Project.objects.get(pk=request.data['project_id'])
#             m = Member(employee=employee, role=role)
#             m.save()
#             project.members.add(m)
#             project.save()
#             return Response({'status': 'OK'}, status=status.HTTP_200_OK)
#         except Exception:
#             return Response({'status': 'Bad Request'}, status=status.HTTP_400_BAD_REQUEST)