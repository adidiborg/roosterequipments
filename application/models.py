from django.db import models
from django.utils import timezone
from datetime import datetime 


class Product(models.Model):
	product = models.CharField(verbose_name='Product Name',max_length=50)
	def __str__(self):
		return self.product

class Subproduct(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	subproduct = models.CharField(verbose_name='Sub Product Name',max_length=50)
	def __str__(self):
		return self.subproduct

class Subsubproduct(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	subproduct = models.ForeignKey(Subproduct,on_delete=models.CASCADE)
	subsubproduct = models.CharField(verbose_name=' Sub Sub Product Name',max_length=50)

class Customer(models.Model):
	customer_name = models.CharField(verbose_name='Customer Name',max_length=50)
	address = models.CharField(verbose_name='Customer Address',max_length=200)
	contact_person = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone = models.CharField(verbose_name='Phone Number',max_length=50)
	GST = models.CharField(max_length=50)
	credit_period = models.IntegerField(verbose_name='Credit Period in Days',)
	def __str__(self):
		return self.customer_name

class Vendor(models.Model):
	vendor_name = models.CharField(verbose_name='Vendor Name',max_length=50)
	address = models.CharField(verbose_name='Vendor Address',max_length=200)
	contact_person = models.CharField(max_length=50)
	email = models.CharField(max_length=50)
	phone = models.CharField(verbose_name='Phone Number',max_length=50)
	GST = models.CharField(max_length=50)
	credit_period = models.IntegerField(verbose_name='Credit Period in Days',)
	def __str__(self):
		return self.vendor_name


class Project(models.Model):
	project_no = models.AutoField(primary_key=True)
	customer_name = models.ForeignKey(Customer,on_delete=models.CASCADE)
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	subproduct = models.ForeignKey(Subproduct,on_delete=models.CASCADE)
	quantity = models.IntegerField()
	start_date = models.DateField(verbose_name='Start Date (YYYY-MM-DD)',default=timezone.now)
	end_date = models.IntegerField(verbose_name='End Date (YYYYMMDD)',)
	present = datetime.now()
	present = int(present.strftime('%Y%m%d'))

	def __str__(self):
		return ("%s , %s , %s , %s , %s" % (self.project_no,self.customer_name,self.subproduct,self.quantity,self.start_date))

class Material(models.Model):
	product = models.ForeignKey(Product,on_delete=models.CASCADE)
	subproduct = models.ForeignKey(Subproduct,on_delete=models.CASCADE)
	part_name = models.CharField(max_length=50)
	raw_material = models.CharField(max_length=50)
	specs_1 = models.CharField(max_length=50)
	specs_2 = models.CharField(max_length=50)
	specs_3 = models.CharField(max_length=50)
	source_1 = models.CharField(max_length=50)
	source_2 = models.CharField(max_length=50)
	quantity = models.CharField(max_length=50)
	lead_time = models.CharField(max_length=20)
	vendor = models.CharField(max_length=20)
	inventory = models.CharField(max_length=20)
	def __str__(self):
		return ("%s , %s , %s" % (self.product,self.subproduct,self.part_name))

# verbose_name=' damping coefficient (kg/s)',
class PurchaseData(models.Model):
	sr_no = models.AutoField(primary_key=True)
	supplier = models.CharField(max_length=50)
	material = models.CharField(max_length=50)
	quantity =models.IntegerField()
	in_date = models.DateField()
	def __str__(self):
		return ("%s , %s , %s,%s,%s" % (self.sr_no,self.supplier,self.material,self.quantity,self.in_date))

class VendorData(models.Model):
	sr_no = models.AutoField(verbose_name='Sr No',primary_key=True)
	out_date = models.DateField(verbose_name='Out Date (YYYY-MM-DD)',)
	vendor_name = models.ForeignKey(Vendor,on_delete=models.CASCADE,verbose_name='Vendor Name',)
	material_provided = models.CharField(verbose_name='Material Provided / Part Name',max_length=50)
	quantity = models.IntegerField(verbose_name='Quantity Provided',)
	purpose = models.CharField(max_length=50)
	quantity_received = models.IntegerField(verbose_name='Quantity Received',)
	in_date = models.DateField(verbose_name='In Date (YYYY-MM-DD)',)			
	def __str__(self):
		return ("%s , %s , %s,%s,%s" % (self.sr_no,self.out_date,self.material_provided,self.quantity,self.in_date))

class Worker(models.Model):
	name = models.CharField(max_length=50)
	def __str__(self):
		return self.name

class Job(models.Model):
	sr_no = models.AutoField(verbose_name='Sr No',primary_key=True)
	date = models.DateField(verbose_name='Date',)
	name = models.ForeignKey(Worker,on_delete=models.CASCADE,verbose_name='Worker Name',)
	part_name = models.CharField(verbose_name='Part Name',max_length=50)
	quantity = models.IntegerField(verbose_name='Quantity',)
	misc = models.CharField(max_length=200)
	def __str__(self):
		return ("%s , %s , %s,%s,%s" % (self.sr_no,self.date,self.name,self.part_name,self.quantity))

class Toggle(models.Model):
	toggle = models.CharField(max_length=10)
	def __str__(self):
		return self.toggle

class Attendance(models.Model):
	date = models.DateField(verbose_name='Date',default=timezone.now,)
	name = models.ForeignKey(Worker,on_delete=models.CASCADE,verbose_name='Worker Name',)
	toggle = models.ForeignKey(Toggle,on_delete=models.CASCADE,verbose_name='Attendance',)
	def __str__(self):
		return ("%s , %s , %s" % (self.date,self.name,self.toggle))