from django.contrib import admin
from django.urls import path
from demo2 import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.main),
    # path('client/', views.filtr),
    # path('search/', views.search),
    # path('sort/', views.sort),
]
