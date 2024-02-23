from django.contrib import admin
from django.urls import path, include
# from layout.views import custom_404


# handler404 = custom_404

urlpatterns = [
    # path('admin/', admin.site.urls),
    path("", include("layout.urls")),
]
