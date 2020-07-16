from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('', include('app.cliente.urls')),
    path('', include('app.funcionario.urls')),
    path('', include('app.produto.urls')),
    path('', include('app.venda.urls')),

]
