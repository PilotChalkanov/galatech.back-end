from django.urls import path

from backend.api.views import ProductListView, SingleProductView, CategoryListView

urlpatterns = (
    path('products/', ProductListView.as_view(), name='shop-products'),
    path('products/<int:pk>', SingleProductView.as_view(), name='single-product'),
    path('product/categories/', CategoryListView.as_view(), name='categories'),
)