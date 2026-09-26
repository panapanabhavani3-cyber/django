from django.urls import path
from myapp import views

urlpatterns = [
    path('', views.index, name='index'),
    path('user/', views.user, name='user'),
    path('product/', views.product, name='product'),
    path('payment/', views.payment, name='payment'),
    path('prediction/', views.prediction, name='prediction'),
    path('report/', views.report, name='report'),
]