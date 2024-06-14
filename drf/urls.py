
from django.contrib import admin
from django.urls import path, include
from rest_framework.documentation import include_docs_urls #Para importar la documentacion


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('api.urls')), 
    path('docs/', include_docs_urls(title='Api Documentatins'))
]
