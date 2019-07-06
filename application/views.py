from django.shortcuts import render
from .models import Project , Material,Attendance,Toggle, Customer,Worker, Subproduct, Product, Vendor, Subsubproduct, VendorData, Job,PurchaseData
from django.shortcuts import render , redirect
from django import forms
from .forms import ProjectForm,AttendanceForm, CustomerForm,WorkerForm, ProductForm, SubproductForm,PurchaseDataForm		, VendorForm, MaterialForm, SubsubproductForm,PurchaseDataForm, VendorDataForm, JobForm
def index(request):
	projects_list=Project.objects.all()
	context={
		'projects_list':projects_list,	
	}	
	return render(request,'index.html',context)

def details(request,project_no):
	materials_list=Material.objects.all()
	context={
		'materials_list':materials_list,	
	}	
	return render(request,'details.html',context)

def materials(request):
	materials_list=Material.objects.all()
	context={
		'materials_list':materials_list,	
	}	
	return render(request,'material.html',context)

def project_new(request):
	if request.method == "POST":
	    form = ProjectForm(request.POST)
	    if form.is_valid():
	        project = form.save(commit=False)
	        project.save()
	        return redirect('/project')
	else:
	    form = ProjectForm()
	return render(request, 'project_edit.html', {'form': form})

def job_new(request):
	if request.method == "POST":
	    form = JobForm(request.POST)
	    if form.is_valid():
	        job = form.save(commit=False)
	        job.save()
	        return redirect('/job')
	else:
	    form = JobForm()
	return render(request, 'job_edit.html', {'form': form})

def worker_new(request):
	if request.method == "POST":
	    form = WorkerForm(request.POST)
	    if form.is_valid():
	        worker = form.save(commit=False)
	        worker.save()
	        return redirect('/job')
	else:
	    form = WorkerForm()
	return render(request, 'worker_edit.html', {'form': form})


def customer(request):
	customers_list=Customer.objects.all()
	context={
		'customers_list':customers_list,	
	}	
	return render(request,'customers.html',context)

def vendor(request):
	vendors_list=Vendor.objects.all()
	context={
		'vendors_list':vendors_list,	
	}	
	return render(request,'vendors.html',context)

def attendance(request):
	attendances_list=Attendance.objects.all()
	context={
		'attendances_list':attendances_list,	
	}	
	return render(request,'attendance.html',context)

def product(request):
	subproducts_list=Subproduct.objects.all()
	context={
		'subproducts_list':subproducts_list,	
	}	
	return render(request,'product.html',context)

def vendordata(request):
	vendors_list=VendorData.objects.all()
	context={
		'vendors_list':vendors_list,	
	}	
	return render(request,'vendordata.html',context)

def purchasedata(request):
	purchasedatas_list=PurchaseData.objects.all()
	context={
		'purchasedatas_list':purchasedatas_list,	
	}	
	return render(request,'purchasedata.html',context)


def job(request):
	jobs_list=Job.objects.all()
	context={
		'jobs_list':jobs_list,	
	}	
	return render(request,'job.html',context)

def customer_new(request):
	if request.method == "POST":
	    form = CustomerForm(request.POST)
	    if form.is_valid():
	        customer = form.save(commit=False)
	        customer.save()
	        return redirect('/customer')
	else:
	    form = CustomerForm()
	return render(request, 'customer_edit.html', {'form': form})

def attendance_new(request):
	if request.method == "POST":
	    form = AttendanceForm(request.POST)
	    if form.is_valid():
	        attendance = form.save(commit=False)
	        attendance.save()
	        return redirect('/attendance')
	else:
	    form = AttendanceForm()
	return render(request, 'attendance_edit.html', {'form': form})

def vendor_new(request):
	if request.method == "POST":
	    form = VendorForm(request.POST)
	    if form.is_valid():
	        vendor = form.save(commit=False)
	        vendor.save()
	        return redirect('/vendor')
	else:
	    form = VendorForm()
	return render(request, 'vendor_edit.html', {'form': form})

def vendordata_new(request):
	if request.method == "POST":
	    form = VendorDataForm(request.POST)
	    if form.is_valid():
	        vendordata = form.save(commit=False)
	        vendordata.save()
	        return redirect('/vendordata')
	else:
	    form = VendorDataForm()
	return render(request, 'vendordata_edit.html', {'form': form})

def purchasedata_new(request):
	if request.method == "POST":
	    form = PurchaseDataForm(request.POST)
	    if form.is_valid():
	        purchasedata = form.save(commit=False)
	        purchasedata.save()
	        return redirect('/purchasedata')
	else:
	    form = PurchaseDataForm()
	return render(request, 'purchasedata_edit.html', {'form': form})

def material_new(request):
	if request.method == "POST":
	    form = MaterialForm(request.POST)
	    if form.is_valid():
	        material = form.save(commit=False)
	        material.save()
	        return redirect('/material')
	else:
	    form = MaterialForm()
	return render(request, 'material_edit.html', {'form': form})

def product_new(request):
	if request.method == "POST":
	    form = ProductForm(request.POST)
	    if form.is_valid():
	       	product = form.save(commit=False)
	        product.save()
	        return redirect('/product')
	else:
	    form = ProductForm()
	return render(request, 'product_edit.html', {'form': form})

def subproduct_new(request):
	if request.method == "POST":
	    form = SubproductForm(request.POST)
	    if form.is_valid():
	        subproduct = form.save(commit=False)
	        subproduct.save()
	        return redirect('/product')
	else:
	    form = SubproductForm()
	return render(request, 'subproduct_edit.html', {'form': form})

def subsubproduct_new(request):
	if request.method == "POST":
	    form = SubsubproductForm(request.POST)
	    if form.is_valid():
	        subsubproduct = form.save(commit=False)
	        subsubproduct.save()
	        return redirect('/product')
	else:
	    form = SubsubproductForm()
	return render(request, 'subsubproduct_edit.html', {'form': form})


def home(request):
	return render(request,'home.html')


	