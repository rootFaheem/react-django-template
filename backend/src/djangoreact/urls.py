from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url('api-auth/', include('rest_framework.urls')),
    url('admin/', admin.site.urls),

]
