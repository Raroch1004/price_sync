from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
]

admin.site.index_title = "Inventory"
admin.site.site_header = "Admin Inventory"
admin.site.site_title = "Site Inventory"

