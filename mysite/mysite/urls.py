from django.contrib import admin
from django.urls import path
from . import views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('AcercaDelProyecto', views.acerca, name='acerca'),
    path('', views.home, name='home'),
    path('base/', views.base, name='base'),
    path('acerca/', views.acerca, name='acerca'),
    path('contacto/', views.contacto, name='contacto'),
    path('costos/', views.costos, name='costos'),
    path('proyecto', views.proyecto, name='proyecto'),
    path('funcionamiento/', views.funcionamiento, name='funcionamiento'),
    path('nosotros/', views.nosotros, name='nosotros'),
]

if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATICFILES_DIRS[0])