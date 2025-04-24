from django.urls import path

from webapp import views
from webapp.views import *

urlpatterns = [
        path('', views.index, name='index'),
        path('repo/<int:project_id>/', views.repo_info, name='repo_info'),

        path('api/feedback', views.feedback, name='feedback')
]
