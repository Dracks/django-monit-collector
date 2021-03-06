"""monitcollector URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add an import:  from blog import urls as blog_urls
    2. Add a URL to urlpatterns:  url(r'^blog/', include(blog_urls))
"""
from django.urls import path

from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('collector', views.collector, name='collector'),
    path('server/<int:server_id>/', views.server, name='server'),
    path('server/<server_id>/process/<process_name>/', views.process, name='process'),
    path('process_action/<int:server_id>/', views.process_action, name='process_action'),
    path('confirm_delete/<int:server_id>/', views.confirm_delete, name='confirm_delete'),
    path('delete_server/<int:server_id>/', views.delete_server, name='delete_server'),

    path('load_system_data/<int:server_id>/', views.load_system_data, name='load_system_data'),
    path('load_process_data/<int:server_id>/<process_name>/', views.load_process_data, name='load_process_data'),
    path('load_dashboard_table/', views.load_dashboard_table, name='load_dashboard_table'),
    path('load_system_table/<int:server_id>/', views.load_system_table, name='load_system_table'),
    path('load_process_table/<int:server_id>/<process_name>/', views.load_process_table, name='load_process_table'),
]
