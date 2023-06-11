from rest_framework import serializers
from rest_framework.generics import ListAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from backend.api.models import Product, ProductCategory


# Create your views here.
class ProductSerializer(serializers.ModelSerializer):
    """Product JSON serializer"""
    class Meta:
        model = Product
        exclude = ('createdTimestamp', 'updatedTimestamp')


class FullProductCategorySerializer(serializers.ModelSerializer):
    """Full category list serializer"""
    product_set = serializers.StringRelatedField(many=True)

    class Meta:
        model = ProductCategory
        fields = '__all__'


class CategoryProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id', 'name')


class ProductListView(ListAPIView):
    """Main shop View for Product"""
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class SingleProductView(RetrieveUpdateDestroyAPIView):
    """The Product View which has all the methods implemented"""
    permission_classes = (AllowAny,)
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CategoryListView(ListAPIView):

    queryset = ProductCategory.objects.all()
    serializer_class = FullProductCategorySerializer