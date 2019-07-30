from django.urls import path
from . import views
urlpatterns=[
    path('',views.return_response,name='get_request_response')
]