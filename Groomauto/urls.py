"""Groomauto URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from django.urls import path
from Groomautoapp import views
admin.site.site_header='Groomauto Admin'
admin.site.site_title='Groomauto Admin Portal'
admin.site.index_title='Welcome To Groomautoapp Admin Panel'
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.Home,name='Home'),
    path('Index/',views.Index,name='Index'),
    path('Contact/',views.Contact,name='Contact'),
    path('Service/',views.Service, name='Service'),
    path('Location/',views.Booking, name='Location'),
    path('Repair/',views.Repair, name='Repair'),
    path('Insurance/',views.Insurance, name='Insurance'),
    path('Feedback/',views.Feedback, name='Feedback'),
    path('Gallery/',views.Gallery, name='Gallery'),
    path('About/',views.About, name='About'),
    path('Joinus/',views.Joinus , name='Login'),
    path('Registation/',views.Registation, name='Registation'),
    path('Profile/',views.Profile_User, name='Profile_User'),
    path('Booking/',views.U_Booking, name='U_Booking'),
    path('Chngpwd/',views.U_Chpwd, name='U_Chpwd'),
    path('Editeprofile/',views.U_Edtprofile, name='U_Edtprofile'),
    path('Repairs/',views.U_Repair, name='U_Repair'),
    path('Vouchers/',views.U_Voucher, name='U_Voucher'),
    path('Services/',views.Services, name='Services'),
    path('Client/',views.Client, name='Client'),
    path('OW_Profile/',views.OW_Profile, name='OW_Profile'),
    path('C_Repair/',views.SCOW_Repair, name='SCOW_Repair'),
    path('OW_Pwd/',views.OW_Pwd, name='OW_Pwd'),
    


]