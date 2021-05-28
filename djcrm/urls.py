
from django.contrib import admin
from django.conf.urls.static import static,settings
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('leads/',include('leads.urls', namespace="leads"))
]
if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL,document_root=settings.STATIC_ROOT)
