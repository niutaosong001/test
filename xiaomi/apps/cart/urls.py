"""xiaomi URL Configuration

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
from apps.cart import views

app_name = "cart"
urlpatterns = [
    path('add', views.CartAddView.as_view(), name='add'),  # 购物车记录添加
    path("", views.ShowView.as_view(), name="show"),  # 显示购物车
    path('update', views.CartUpdateView.as_view(), name='update'),  # 购物车记录更新
    path('delete', views.CartDeleteView.as_view(), name='delete'),  # 购物车记录删除
]
