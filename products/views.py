from django.db.models import Q
from rest_framework import generics
# from rest_framework.decorators import api_view

from products.models import Category, Product
from products.serializers import CategorySerializer, ProductSerializer


class LatestProductList(generics.ListAPIView):
    queryset = Product.objects.order_by('-id').all()[0:4]
    serializer_class = ProductSerializer


class ProductDetailView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    lookup_field = 'slug'


class CategoryDetailView(generics.RetrieveAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer
    lookup_field = 'slug'


class CategoryList(generics.ListAPIView):
    queryset = Category.objects.all()
    serializer_class = CategorySerializer


# @api_view('POST')
# def search(request):
#     query = request.data.get('query', '')

#     if query:
#         products = Product.objects.filter(
#             Q(name__icontains=query) |
#             Q(description__icontains=query)
#         )

class SearchList(generics.ListAPIView):
    serializer_class = ProductSerializer

    def get_queryset(self):
        queryset = Product.objects.all()
        query = self.request.query_params.get('query')
        if query:
            queryset = Product.objects.filter(
                Q(name__icontains=query) |
                Q(description__icontains=query)
            )
        return queryset
