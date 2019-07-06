"""djangoproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from application import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.home,name='home'),
    path('project/',views.index,name='index'),
    path('material/',views.materials,name='materials'),
    path('customer/',views.customer,name='customer'),
    path('vendor/',views.vendor,name='vendor'),
    path('vendordata/',views.vendordata,name='vendordata'),
    path('purchasedata/',views.purchasedata,name='purchasedata'),
    path('product/',views.product,name='product'),
    path('job/',views.job,name='job'),
    path('attendance/',views.attendance,name='attendance'),
    path('attendance/new/', views.attendance_new, name='attendance_new'),
    path('project/new/', views.project_new, name='project_new'),
    path('worker/new/', views.worker_new, name='worker_new'),
    path('purchasedata/new/', views.purchasedata_new, name='purchasedata_new'),
    path('job/new/', views.job_new, name='job_new'),
    path('customer/new/', views.customer_new, name='customer_new'),
    path('vendor/new/', views.vendor_new, name='vendor_new'),
    path('product/new/', views.product_new, name='product_new'),
    path('vendordata/new/', views.vendordata_new, name='vendordata_new'),
    path('subproduct/new/', views.subproduct_new, name='subproduct_new'),
    path('subsubproduct/new/', views.subsubproduct_new, name='subsubproduct_new'),
    path('material/new/', views.material_new, name='material_new'),
    path('<int:project_no>/',views.details,name='details'),
]
