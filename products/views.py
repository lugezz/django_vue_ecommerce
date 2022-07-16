from rest_framework import generics

from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer


class LatestProductList(generics.ListAPIView):
    queryset = Product.objects.order_by('-id').all()[0:4]
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
