from django.contrib import admin
from django.urls import path, include
from django.views.generic import TemplateView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello-webpack/', TemplateView.as_view(template_name='hello_webpack.html')),
    path('api/', include('woker.api.urls'))
]
