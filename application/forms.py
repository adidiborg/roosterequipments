from django import forms
from django.forms import DateInput
from django.contrib.admin import widgets
from .models import Project, Customer,Worker,Attendance,Toggle, Product, Subproduct,Job, Vendor, Material,PurchaseData, Subsubproduct, VendorData

class ProjectForm(forms.ModelForm):

    class Meta:
        model = Project
        fields = ('customer_name', 'product','subproduct','quantity','start_date','end_date')

class MaterialForm(forms.ModelForm):

    class Meta:
        model = Material
        fields = ('product', 'subproduct','part_name','raw_material','specs_1','specs_2','specs_3','source_1','source_2','quantity','lead_time')

class CustomerForm(forms.ModelForm):

    class Meta:
        model = Customer
        fields = ('customer_name', 'address','contact_person','email','phone','GST','credit_period')

class PurchaseDataForm(forms.ModelForm):

    class Meta:
        model = PurchaseData
        fields = ('sr_no', 'supplier','material','quantity','in_date')

class VendorForm(forms.ModelForm):

    class Meta:
        model = Vendor
        fields = ('vendor_name', 'address','contact_person','email','phone','GST','credit_period')


class VendorDataForm(forms.ModelForm):

    class Meta:
        model = VendorData
        fields = ('sr_no', 'out_date','vendor_name','material_provided','quantity','purpose','quantity_received','in_date')

class JobForm(forms.ModelForm):

    class Meta:
        model = Job
        fields = ('sr_no', 'date','name','part_name','quantity','misc')

class WorkerForm(forms.ModelForm):

    class Meta:
        model = Worker
        fields = ('name',)

class AttendanceForm(forms.ModelForm):

    class Meta:
        model = Attendance
        fields = ('date','name','toggle')

class ProductForm(forms.ModelForm):

    class Meta:
        model = Product
        fields = ('product',)

class SubproductForm(forms.ModelForm):

	class Meta:
	    model = Subproduct
	    fields = ('product','subproduct')

class SubsubproductForm(forms.ModelForm):

    class Meta:
        model = Subsubproduct
        fields = ('product','subproduct','subsubproduct')
