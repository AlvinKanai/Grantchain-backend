from rest_framework.generics import RetrieveAPIView, ListAPIView
from rest_framework import permissions
from .models import Ecosystem
from .serializers import EcosystemSerializer

# Create your views here.
class EcosystemListView(ListAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Ecosystem.objects.all()
    serializer_class = EcosystemSerializer
    pagination_class = None


class EcosystemView(RetrieveAPIView):
    permission_classes = (permissions.AllowAny, )
    queryset = Ecosystem.objects.all()
    serializer_class = EcosystemSerializer


