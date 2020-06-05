
from . import views
from django.urls import path

urlpatterns = [
    
    path('', views.index,name='index'),
    path('about',views.about,name='about'),
    path('profile',views.profile,name='profile'),
    path('payment_status',views.payment_status,name="payment_status")
    
]
