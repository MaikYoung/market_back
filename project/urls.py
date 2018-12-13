"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls

from admins.views import AdminDetail
from stores.views import StoreListView, StoreDetailView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('docs/', include_docs_urls(title='Market-Docs')),
    # API for admins store (users)
    path('user/', include('rest_auth.urls')),
    path('user/registration/', include('rest_auth.registration.urls')),
    path('users/<int:pk>/', AdminDetail.as_view(), name='user-detail'),
    # API for stores
    path('stores', StoreListView.as_view(), name='stores-list'),
    path('store/<int:pk>', StoreDetailView.as_view(), name='store-detail')
]
