from django.db import models
from datetime import date
from django.utils import timezone
# Create your models here.

class package(models.Model):
	"""Field Name"""
	c_id = models.AutoField(primary_key=True)
	co_name = models.CharField(max_length=500)
	c_price = models.DecimalField(max_digits=6,decimal_places=2)

class gallery(models.Model):
	imgname = models.CharField(primary_key=True, max_length=50)
	image = models.ImageField(upload_to='gallery_pic')

class service_center(models.Model):
	"""Field Name"""
	sc_name = models.CharField(primary_key=True,max_length=30)
	mobile_no = models.CharField(max_length=12)
	area = models.CharField(max_length=15)
	city = models.CharField(max_length=12)
	zipcode = models.CharField(max_length=6)
	image = models.ImageField(upload_to='sc_image',blank=True)
	sc_address = models.CharField(max_length=60)

class company(models.Model):
	"""Field Name"""
	c_id = models.CharField(max_length=2)
	c_name = models.CharField(max_length=50,primary_key=True)
	
class model(models.Model):
	"""Field Name"""
	m_id = models.CharField(max_length=2)
	m_name = models.CharField(max_length=15,primary_key=True)
	c_name = models.ForeignKey('company',on_delete=models.PROTECT)

class contact(models.Model):
	"""Table Field Name"""
	c_id = models.AutoField(primary_key=True)
	c_name = models.CharField(max_length=30)
	mobile_no = models.CharField(max_length=12)
	subject = models.CharField(max_length=50)
	msg = models.CharField(max_length=150)

class feedback(models.Model):
	"""Table Fields Name"""
	f_id = models.AutoField(primary_key=True)
	name = models.CharField(max_length=30)
	mail_id = models.EmailField(max_length=30)
	mobile_no = models.CharField(max_length=12)
	msg = models.CharField(max_length=60)

class u_detail(models.Model):
	"""Table Fields Name"""
	u_id = models.AutoField(primary_key=True)
	area = models.CharField(max_length=30,default='Ghatlodiya')
	pincode = models.CharField(max_length=6,default='380061')
	address = models.CharField(max_length=50,default='Ahm')

class ow_detail(models.Model):
	"""Table Fields Name"""
	ow_id = models.AutoField(primary_key=True)
	contact = models.CharField(max_length=12)
	sc_address = models.CharField(max_length=50)
	area = models.CharField(max_length=15)
	pincode = models.CharField(max_length=5,blank=True)
	city = models.CharField(max_length=12)
	

class booking(models.Model):
	"""Table Field Name"""
	b_id = models.AutoField(primary_key=True)
	f_name = models.CharField(max_length=10)
	l_name = models.CharField(max_length=10)
	email = models.EmailField(max_length=30)
	m_no = models.CharField(max_length=12)
	area = models.CharField(max_length=12)
	pincode = models.CharField(max_length=6)
	address = models.CharField(max_length=100)
	p_time = models.DateField(default=timezone.now(),blank=True)
	price = models.DecimalField(max_digits=5,decimal_places=2)
	sc_name = models.ForeignKey("service_center",on_delete=models.PROTECT)
	sc_address = models.CharField(max_length=150)
	c_name = models.ForeignKey("company",on_delete=models.PROTECT)
	m_name = models.ForeignKey("model",on_delete=models.PROTECT)
	s_date = models.DateField(default=date.today)
	v_number = models.CharField(max_length=20)


class Repair(models.Model):
	v_type =(
		('Hero','Hero'),
		('Honda','Honda'),
		('Bajaj','Bajaj'),
		('Tvs','Tvs'),
		('Yamaha','yamaha'),
		('suzuki','suzuki'),
		('KTM','KTm'),
	)


	name= models.CharField(max_length=64)
	email = models.EmailField(default='')
	phone = models.CharField(max_length=12)
	vehicle_company = models.CharField(max_length=64,choices=v_type)
	vehicle_model = models.CharField(max_length=64)
	repair_date = models.DateField(blank=True, null=True)
	vehicle_number = models.CharField(max_length=64)
	add_message = models.TextField()

	def __str__(self):
		return self.name



