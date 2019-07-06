from django.contrib import admin
from .models import Product, Subproduct,Toggle,Attendance, Customer, Project, Material, Vendor,Job,Worker, Subsubproduct, PurchaseData, VendorData
from django.contrib.auth.models import Group

admin.site.register(Product)
admin.site.register(Job)
admin.site.register(Toggle)
admin.site.register(Attendance)
admin.site.register(Worker)
admin.site.register(Subproduct)
admin.site.register(Customer)
admin.site.register(PurchaseData)
admin.site.register(VendorData)
admin.site.register(Project)
admin.site.register(Material)
admin.site.register(Vendor)
admin.site.register(Subsubproduct)
admin.site.unregister(Group)