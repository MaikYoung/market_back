
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
