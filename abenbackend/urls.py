from django.conf import settings
from django.contrib import admin
from django.urls import include, path

from common.views import dashboard, logout, subscription, cancel_sub

urlpatterns = [
    path("admin/", admin.site.urls),
    path("logout", logout, name="logout"),
    path("accounts/", include("django_registration.backends.one_step.urls")),
    path(
        "auth/",
        include("django.contrib.auth.urls"),
    ),
    path("accounts/profile/", dashboard, name="profile"),
    path("subscribe-page", subscription, name="subscribe_page"),
    path("cancel_sub", cancel_sub, name="cancel_sub"),
]
