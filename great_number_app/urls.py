from django.urls import path
from . import views

urlpatterns = [
    path('', views.root),
    path('process', views.process),
    path('clear', views.destroy_session),
    path('restart', views.destroy_session),
    path('success', views.success),
    path('congrats', views.congrats_page)
]