from django.urls import path, include
from django.conf.urls import url
from rest_framework.generics import CreateAPIView, DestroyAPIView
from .views import *

api_urls = [
    url(r'^rest-auth/', include('rest_auth.urls')),
    path('events/get/', GetEventsView.as_view(), name='get_events'),
    path('events/get_contract_ex/', GetEventContractExView.as_view(), name='get_contract'),
    path('user/data/', GetUserDataView.as_view(), name='get_user_data'),
    path('user/update/<pk>/', UpdateUserDataView.as_view(), name='update_user_data'),

    path('app/get/', GetApplicationsView.as_view(), name='app_get'),
    path('app/create/', CreateApplicationView.as_view(), name='app_create'),

    path('stages/1/get/', GetStage1View.as_view(), name='stage_1_get'),
    path('stages/2/get/', GetStage2View.as_view(), name='stage_2_get'),
    path('stages/3/get/', GetStage3View.as_view(), name='stage_3_get'),
    path('stages/4/get/', GetStage4View.as_view(), name='stage_4_get'),

    path('stages/1/upd/<pk>/', CreateStage1View.as_view(), name='stage_1_create'),
    path('stages/2/upd/<pk>/', CreateStage2View.as_view(), name='stage_2_create'),
    path('stages/3/upd/<pk>/', CreateStage3View.as_view(), name='stage_3_create'),
    path('stages/4/upd/<pk>/', CreateStage4View.as_view(), name='stage_4_create'),
]
