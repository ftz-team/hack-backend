from django.urls import path, include
from django.conf.urls import url
from rest_framework.generics import CreateAPIView, DestroyAPIView
from .views import *

api_urls = [
    url(r'^rest-auth/', include('rest_auth.urls')),
    path('events/get/', GetEventsView.as_view(), name='get_events'),
    path('user/data/', GetUserDataView.as_view(), name='get_user_data'),
]