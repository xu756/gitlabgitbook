from django.urls import path

from webapp import views
from webapp.views import *

urlpatterns = [
        path('', views.index, name='index'),
        path('api/feedback', views.feedback, name='feedback')
]
