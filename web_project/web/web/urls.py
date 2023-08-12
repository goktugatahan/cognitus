from django.contrib import admin
from django.urls import path, include
from webapp import urls as django_urls
from dashboard import urls as dashboard_urls


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/datas/', include(django_urls)),
    path('dashboard/', include(dashboard_urls))
]
