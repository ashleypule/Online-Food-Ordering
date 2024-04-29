from django.contrib.auth import views
from django.urls import path

from core.views import frontpage, signup, menu, myaccount, edit_myaccount
from product.views import product
from .views import MapView

urlpatterns = [
    path('', frontpage, name='frontpage'),
    path('signup/', signup, name='signup'),
    path('login/', views.LoginView.as_view(template_name='core/login.html'), name='login'),
    path('myaccount/', myaccount, name='myaccount'),
    path('menu/', menu, name='menu'),
    path('menu/<slug:slug>', product, name='product'),
    path('map/', MapView.as_view(), name='map'),
]

