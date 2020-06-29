from django.urls import path
from . import views

urlpatterns = [
    path('', views.checkout, name='checkout'),
    path('checkout/<order_number>', views.checkout, name='checkout_success'),
]
