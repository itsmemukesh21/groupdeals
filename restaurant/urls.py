from django.urls import include, path
from .views import *

urlpatterns = [
    path('',Homepage.as_view(),name="Homepage"),
    path('sign-up',SignUp.as_view(),name="signup"),
    path('login',Login.as_view(),name="login"),
    path('product',Product.as_view(),name="product")
]