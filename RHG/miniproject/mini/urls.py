# urls.py
from django.urls import path
from . import views

urlpatterns = [
	path('ide/', views.IDE.as_view(), name = 'mini_IDE'),
	path('dashboard/', views.Dashboard.as_view(), name = 'mini_dashboard'),
]
