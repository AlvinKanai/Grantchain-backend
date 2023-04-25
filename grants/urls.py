from django.urls import path
from .views import GrantsListView, GrantView, SearchView

urlpatterns = [
    path('', GrantsListView.as_view()),
    path('search', SearchView.as_view()),
    path('<slug>', GrantView.as_view()),
]
