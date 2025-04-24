from django.urls import path

from webapp import views
from webapp.views import *

urlpatterns = [
        path('', views.index, name='index'),

    # path('stock_data/', stock_data_view, name='stock_data_view'),
    # 添加路径参数
    # path('stock_data/<str:company_name>/', stock_data_view, name='stock_data_view'),
    # path('moving_average/<str:company_name>/', get_moving_average_view, name='get_moving_average_view'),
    # path('daily_return/<str:company_name>/', daily_return_view, name='daily_return_view'),
    # path('save_stock_data/<str:company_name>/', save_stock_data, name='save_stock_data'),
]
