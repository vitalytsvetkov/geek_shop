from django.contrib import admin
from django.urls import path
from mainapp import views as mainapp
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', mainapp.main, name='main'),
    path('products/', mainapp.products, name='products'),
    path('contact/', mainapp.contacts, name='contacts'),
    path('admin/', admin.site.urls),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)