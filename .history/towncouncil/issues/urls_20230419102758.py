from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("submit/", views.submit_issue, name="submit_issue"),
    # path("thankyou/", views.thank_you, name="thank_you"), 
] 