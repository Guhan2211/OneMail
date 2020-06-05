
from django.contrib import admin
from django.urls import path,include

urlpatterns = [
    path('',include('pages.urls')),
    path('admin/', admin.site.urls),
    path('accounts/',include('allauth.urls')),
    path('es/',include('es.urls')),
    path('tinymce/',include('tinymce.urls')),
]
