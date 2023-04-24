from django.urls import path
from .views import EcosystemListView, EcosystemView

urlpatterns = [
    path('', EcosystemListView.as_view()),
    path('<pk>', EcosystemView.as_view()),
]
