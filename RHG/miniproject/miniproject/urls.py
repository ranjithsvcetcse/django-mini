
from django.contrib import admin
from django.urls import path, include
# from mini import urls as mini_urls
urlpatterns = [
    path('admin/', admin.site.urls),
    path('mini/', include('mini.urls')),

]
