from django.urls import path

from . import views


urlpatterns = [
    path("", views.index, name="index"),
    path("submit/", views.submit_issue, name="submit_issue"),
    path("thankyou/", views.thank_you, name="thank_you"),
    path("issues/", views.list_issues, name="list_issues"),
    path("issues/<str:issue_id>", views.display_issue, name="display_issue"),
    path("login/", views.login_responder, name="login_responder"),
    path("logout/", views.logout_responder, name="logout_responder")
]


from django.conf.urls.static import static
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)