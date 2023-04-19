from django.urls import include, path
from django.conf.urls.static import static
import settings

urlpatterns = [
    path('', include('issues.urls')),
    static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
]