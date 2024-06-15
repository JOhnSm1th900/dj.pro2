import debug_toolbar
from django.contrib import admin
from django.urls import path, include



admin.site.site_header = ('Projects Management')
admin.site.site_title = ('Projects Management')

urlpatterns = [
    path('__debug__/', include(debug_toolbar.urls)),
    path('', include('Project.urls')),
    path('accounts/', include('accounts.urls')),
    path('admin/', admin.site.urls),
]
