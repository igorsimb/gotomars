from allauth.account.models import EmailAddress
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sites.models import Site
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    # Local apps
    path("", include("core.urls")),
    # Third-party apps
    path("__debug__/", include("debug_toolbar.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

admin.site.unregister(Site)
admin.site.unregister(EmailAddress)
