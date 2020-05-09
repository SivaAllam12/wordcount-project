
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.homefn,name='home'),
    path('countpage/',views.countfn,name='count'),
    path('aboutpage/',views.aboutfn,name='about')
]