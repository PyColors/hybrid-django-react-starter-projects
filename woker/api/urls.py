from rest_framework import routers
from . import views


urlpatterns = [
    # other urls here
]

router = routers.DefaultRouter()
router.register('api/employees', views.EmployeeViewSet, basename='woker')
router.register(r'', views.EmployeeViewSet, basename='woker')

urlpatterns += router.urls
