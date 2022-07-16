from django.urls import path

from products.views import LatestProductList, ProductDetailView


urlpatterns = [
    # path('', ArticleListView.as_view(), name='article-list'),
    path('latest-products/', LatestProductList.as_view(), name='latest-products'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
]
