from django.urls import include, path
from django.conf.urls.static import static

urlpatterns = [
    path('', include('issues.urls')),
]