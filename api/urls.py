#from django.urls import path, include
#from rest_framework import routers
#from api import views
#
#router = routers.DefaultRouter()
#router(r'programmers', views.ProgrammerViewSet)
#
#urlpatterns =[
#    path('', include(router.urls))
#]

# api/urls.py
from django.urls import path, include
from rest_framework import routers
from . import views

router = routers.DefaultRouter()
router.register(r'programmers', views.ProgrammerViewSet)  # Registrar ProgrammerViewSet en el router

urlpatterns = [
    path('api/v1/', include(router.urls)),  # Incluir las URLs generadas por el router en las URLs de la aplicación
]
