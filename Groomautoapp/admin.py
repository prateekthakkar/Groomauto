from django.contrib import admin
from .models import *

# Register your models here.

class galleryadmin(admin.ModelAdmin):
	list_display = ['imgname','image']
admin.site.register(gallery,galleryadmin)

class packageadmin(admin.ModelAdmin):
 	list_display=['c_id','c_price','co_name']
admin.site.register(package,packageadmin)

class service_centeradmin(admin.ModelAdmin):
 	list_display=['sc_name','mobile_no','area','city','zipcode','sc_address']
admin.site.register(service_center,service_centeradmin)

class companyadmin(admin.ModelAdmin):
 	list_display=['c_id','c_name']
admin.site.register(company,companyadmin)

class modeladmin(admin.ModelAdmin):
 	list_display=['m_id','m_name','c_name']
admin.site.register(model,modeladmin)

class contactadmin(admin.ModelAdmin):
 	list_display=['c_id','c_name','mobile_no','subject','msg']
admin.site.register(contact,contactadmin)

class feedbackadmin(admin.ModelAdmin):
 	list_display=['f_id','name','mail_id','mobile_no','msg']
admin.site.register(feedback,feedbackadmin)

class u_loginadmin(admin.ModelAdmin):
 	list_display=['u_id','area','pincode','address']
admin.site.register(u_detail,u_loginadmin)

class bookingadmin(admin.ModelAdmin):
	list_display=['b_id','f_name','l_name','email','m_no','area','pincode','address',
	'p_time','price','sc_name','sc_address','c_name','m_name','s_date','v_number']
admin.site.register(booking,bookingadmin)


class repairadmin(admin.ModelAdmin):
	list_display=['name','email','phone','vehicle_company','vehicle_model'
	,'repair_date','vehicle_number','add_message']		
admin.site.register(Repair,repairadmin)

class ow_detailadmin(admin.ModelAdmin):
	list_display=['ow_id','contact','sc_address','area','pincode','city']
admin.site.register(ow_detail,ow_detailadmin)
		