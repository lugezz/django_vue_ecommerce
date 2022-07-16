from django.urls import path

from products.views import CategoryDetailView, LatestProductList, ProductDetailView


urlpatterns = [
    # path('', ArticleListView.as_view(), name='article-list'),
    path('latest-products/', LatestProductList.as_view(), name='latest-products'),
    path('<slug:slug>/', ProductDetailView.as_view(), name='product-detail'),
    path('category/<slug:slug>/', CategoryDetailView.as_view(), name='category-detail'),
]
