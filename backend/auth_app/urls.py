from django.urls import path, include

from backend.api.views import ProductListView

urlpatterns = (
    path('', ProductListView.as_view(), name='invalid'),
)