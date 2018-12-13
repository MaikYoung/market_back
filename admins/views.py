from rest_framework import status
from rest_framework.generics import RetrieveUpdateDestroyAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from admins.models import Admin
from admins.serializers import AdminSerializer


class AdminDetail(RetrieveUpdateDestroyAPIView):
    queryset = Admin.objects.all()
    serializer_class = AdminSerializer
    permission_classes =[IsAuthenticated]

    """
    Devuelve el objeto admin solo si el user de la petición corresponde a ese objeto, si no 401
    """

    def retrieve(self, request, *args, **kwargs):
        object = self.get_object()
        if object.id == self.request.user.id:
            serializer = AdminSerializer(object)
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(status=status.HTTP_401_UNAUTHORIZED)

