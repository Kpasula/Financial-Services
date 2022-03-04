from rest_framework.urlpatterns import format_suffix_patterns

from . import views
from django.urls import path, re_path

app_name = 'portfolio'
urlpatterns = [
    path('', views.home, name='home'),
    re_path(r'^home/$', views.home, name='home'),
    path('customer_list', views.customer_list, name='customer_list'),
    path('customer/<int:pk>/edit/', views.customer_edit, name='customer_edit'),
    path('customer/<int:pk>/delete/', views.customer_delete, name='customer_delete'),
    path('customer/create/', views.customer_new, name='customer_new'),
    path('stock_list', views.stock_list, name='stock_list'),
    path('stock/create/', views.stock_new, name='stock_new'),
    path('stock/<int:pk>/edit/', views.stock_edit, name='stock_edit'),
    path('stock/<int:pk>/delete/', views.stock_delete, name='stock_delete'),
    path('investment_list', views.investment_list, name='investment_list'),
    path('investment/create/', views.investment_new, name='investment_new'),
    path('investment/<int:pk>/edit/', views.investment_edit, name='investment_edit'),
    path('investment/<int:pk>/delete/', views.investment_delete, name='investment_delete'),
    path('customer/<int:pk>/portfolio/', views.portfolio, name='portfolio'),
    re_path(r'^customers_json/', views.CustomerList.as_view()),
    path('customer/<int:pk>/portfolio/portfolio_pdf/', views.portfolio_pdf, name='portfolio_pdf'),
    re_path(r'^mutualfund/$', views.mutual_funds_list, name='mutual_funds_list'),
    re_path(r'^mutualfund/(?P<pk>\d+)/delete/$', views.mutual_funds_delete, name='mutual_funds_delete'),
    re_path(r'^mutualfund/(?P<pk>\d+)/edit/$', views.mutual_funds_edit, name='mutual_funds_edit'),
    re_path(r'^mutualfund/create/$', views.mutual_funds_new, name='mutual_funds_new'),
]

urlpatterns = format_suffix_patterns(urlpatterns)
