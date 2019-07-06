from django.contrib import admin
from django.urls import path,include
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.index,name='index'),
    path('<int:project_no>/',views.details,name='details'),
]
