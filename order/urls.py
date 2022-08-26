from django.urls import path

from order.views import checkout, OrdersList

urlpatterns = [
    path('checkout/', checkout),
    path('', OrdersList.as_view()),
]
