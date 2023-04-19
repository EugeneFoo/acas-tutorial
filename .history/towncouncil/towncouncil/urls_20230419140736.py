from django.urls import include, path
from django.conf.urls.static import static
from settings import PROJECT_ROOT

urlpatterns = [
    path('', include('issues.urls')),
    static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
]