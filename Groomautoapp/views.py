from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login
from django.shortcuts import redirect
from .models import feedback, contact, booking, Repair
from django.contrib.auth.decorators import login_required
# Create your views here.

@login_required
def special(request):
    return HttpResponse("You are logged in !")

@login_required
def logout(request):
    logout(request)
    return HttpResponseRedirect(reverse('welcome'))

def Home(request):
    return render(request,'Groomautoapp/Home.html')

def Index(request):
    return render(request,'Groomautoapp/Index.html')

def Contact(request):
    if request.method == 'POST':
        c_name = request.POST.get('c_name', '')
        mobile_no = request.POST.get('mobile_no', '')
        subject = request.POST.get('subject','')
        msg = request.POST.get('msg', '')
        Cont = contact(c_name=c_name, mobile_no=mobile_no, subject=subject, msg=msg)
        Cont.save()
    return render(request,'Groomautoapp/Contact.html')
def Service(request):
    return render(request,'Groomautoapp/Service.html')

def Booking(request):
    if request.method =='POST':
        b_id = request.POST.get('b_id','')
        f_name = request.POST.get('f_name','')
        l_name = request.POST.get('l_name', '')
        email  = request.POST.get('email ', '')
        m_no  = request.POST.get('m_no ', '')
        area  = request.POST.get('area ', '')
        pincode  = request.POST.get('pincode ', '')
        address  = request.POST.get('address ', '')
        p_time  = request.POST.get('p_time', '')
        price  = request.POST.get('price ', '')
        sc_name  = request.POST.get('sc_name ', '')
        sc_address  = request.POST.get('sc_address ', '')
        c_name  = request.POST.get('c_name ', '')
        m_name  = request.POST.get('m_name ', '')
        s_date  = request.POST.get('s_date ', '')
        v_number  = request.POST.get('v_number  ', '')
        book = booking(b_id=b_id,f_name=f_name, l_name=l_name, email=email, m_no=m_no
                       , area=area,pincode=pincode, address=address,p_time=p_time
                       , price=price, sc_name=sc_name,sc_address=sc_address, c_name=c_name, m_name=m_name,s_date=s_date, v_number=v_number)
        book.save()
    return render(request,'Groomautoapp/Location.html')

def Repair(request):
     if request.method =='POST':
        fname= request.POST.get('name','')
        email= request.POST.get('email','')
        phone = request.POST.get('phone','')
        vehicle_company = request.POST.get('vehicle_company','')
        vehicle_model = request.POST.get('vehicle_model','')
        repair_date = request.POST.get('repair_date','')
        vehicle_number = request.POST.get('vehicle_number','')
        add_message = request.POST.get('add_message','')
        repair = Repair(name = name, email = email, phone = phone,vehicle_company = vehicle_company, vehicle_model = vehicle_model, repair_date = repair_date, vehicle_number = vehicle_number, add_message = add_message)
        repair.save()
     return render(request,'Groomautoapp/Repair.html')

def Insurance(request):
    return render(request,'Groomautoapp/Insurance.html')

def Feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name','')
        mail_id = request.POST.get('mail_id','')
        mobile_no = request.POST.get('mobile_no','')
        msg = request.POST.get('msg','')
        feed = feedback(name=name, mail_id=mail_id, mobile_no=mobile_no, msg=msg)
        feed.save()
   
    return render(request,'Groomautoapp/Feedback.html')

def Gallery(request):
    return render(request,'Groomautoapp/Gallery.html')

def About(request):
    return render(request,'Groomautoapp/About.html')


def Registation(request):
    if request.method == 'POST' :
        uname = request.POST.get('username','')
        fname = request.POST.get('fname','')
        lname = request.POST.get('lname','')
        email = request.POST.get('email','')
        password = request.POST.get('password','')
        user = User.objects.create_user(username=uname , fname=fname , lname=lname , email=email , password=password)
        user.save()
    return render(request,'Groomautoapp/Registation.html')


def Joinus(request):

    if request.method == 'POST' :
        email = request.POST.get('email','')
        password = request.POST.get('pass','')
        user = authenticate(request , email=email , password=password)
        if user is not None:
            msg = 'valid user'
            login(request , user)
            return redirect('Index')
        else :
            msg = 'invalid user'
        context = {
            'msg' : msg
        }
    return render(request,'Groomautoapp/Login.html')

def U_Booking(request):
    return render(request,'Groomautoapp/User_Side/book.html')

def U_Chpwd(request):
    return render(request,'Groomautoapp/User_Side/change_password.html')

def U_Edtprofile(request):
    return render(request,'Groomautoapp/User_Side/Edit_Profile.html')

def Profile_User(request):
    return render(request,'Groomautoapp/User_Side/Profile_User.html')

def U_Repair(request):
    return render(request,'Groomautoapp/User_Side/repair.html')


def U_Voucher(request):
    return render(request,'Groomautoapp/User_Side/Vouchar.html')

def Services(request):
    return render(request,'Groomautoapp/SC_OWNER/Home.html')

def Client(request):
    return render(request,'Groomautoapp/SC_OWNER/Client.html')

def OW_Profile(request):
    return render(request,'Groomautoapp/SC_OWNER/Profile.html')

def SCOW_Repair(request):
    return render(request,'Groomautoapp/SC_OWNER/Repair.html')

def OW_Pwd(request):
    return render(request,'Groomautoapp/SC_OWNER/chw_pwd.html')

































