from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView
from rest_framework import permissions
from .models import Grant
from .serializers import GrantSerializer, GrantDetailSerializer
from datetime import datetime, timezone, timedelta
# Create your views here.

class GrantsListView(ListAPIView):
    queryset = Grant.objects.order_by('-date_added').filter(is_published=True)
    permission_classes = (permissions.AllowAny, )
    serializer_class = GrantSerializer
    lookup_field = 'slug'

class GrantView(RetrieveAPIView):
    queryset = Grant.objects.order_by('-date_added').filter(is_published=True)
    permission_classes = (permissions.AllowAny, )
    serializer_class = GrantDetailSerializer
    lookup_field = 'slug'

class SearchView(APIView):
    permission_classes = (permissions.AllowAny, )
    serializer_class = GrantSerializer

    def post(self, request, format=None):
        queryset = Grant.objects.order_by('-date_added').filter(is_published=True)
        data = self.request.data

        grant_type = data['grant_type']
        queryset = queryset.filter(grant_type__iexact=grant_type)

        # ecosystem = data['ecosystem']
        # queryset = queryset.filter(ecosystem__exact=ecosystem)

        project_category = data['project_category']
        queryset = queryset.filter(project_category__iexact=project_category)

        days_passed = data['date_added']
        if days_passed == '1 or less':
            days_passed = 1
        elif days_passed == '2 or less':
            days_passed = 2
        elif days_passed == '5 or less':
            days_passed = 5
        elif days_passed == '10 or less':
            days_passed = 10
        elif days_passed == '20 or less':
            days_passed = 20
        elif days_passed == 'Any':
            days_passed = 0

        for query in queryset:
            num_days = (datetime.now(timezone.utc) - query.date_added).days

            if days_passed !=0:
                if num_days > days_passed:
                    slug=query.slug
                    queryset = queryset.exclude(slug__iexact=slug)

        keywords = data['keywords']
        queryset = queryset.filter(description__icontains=keywords)

        serializer = GrantSerializer(queryset, many=True)

        return Response(serializer.data)
