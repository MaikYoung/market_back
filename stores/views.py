from rest_framework import status
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.pagination import PageNumberPagination
from rest_framework.response import Response

from stores.models import Store
from stores.serializers import StoreListSerializer, StoreDetailSerializer


class StoreListView(ListAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreListSerializer
    pagination_class = PageNumberPagination
    permission_classes = []


class StoreDetailView(RetrieveUpdateDestroyAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer
    permission_classes = []

    def retrieve(self, request, *args, **kwargs):
        store = self.get_object()
        serializer = StoreDetailSerializer(store)
        return Response(serializer.data, status=status.HTTP_200_OK)


