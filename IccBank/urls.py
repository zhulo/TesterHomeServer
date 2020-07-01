from django.urls import path
from . import views

urlpatterns = [
    path('create_address', views.post_create_address,),
    path('check_address', views.post_check_address, ),
    path('add_address', views.post_add_address, ),
    path('agentPay_proxyPay', views.post_agentPay_proxyPay, ),
    path('query_agentPay', views.post_agentPay_query, ),
]
