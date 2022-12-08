from django.shortcuts import render, redirect
from .models import *
from django.contrib.auth.models import User, Group
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponse
from django.utils import timezone

def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')



def createaccountpage(request):
    message = ''
    user = 'none'
    if request.method == "POST":
        iin = request.POST['iin']
        name = request.POST['name']
        surname = request.POST['surname']
        middlename = request.POST['middlename']
        gender = request.POST['gender']
        birthday = request.POST['birthday']
        phone_number = request.POST['phone_number']
        emergency_contact = request.POST['emergency_contact']
        email = request.POST['email']
        address = request.POST['address']
        blood_group = request.POST['blood_group']
        maritual_status = request.POST['maritual_status']
        password = request.POST['password']
        repeatedpassword = request.POST['repeatedpassword']

        try:
            if password == repeatedpassword:
                Patient.objects.create(iin = iin, name = name, surname = surname, middlename = middlename, gender = gender, birthday = birthday, phone_number = phone_number, emergency_contact = emergency_contact,email = email, address = address, blood_group = blood_group, maritual_status = maritual_status)
                user = User.objects.create_user(first_name = name, email=email, password= password, username=iin)
                pat_group = Group.objects.get(name='Patient')
                pat_group.user_set.add(user)
                user.save()
                message = 'no'
            else:
                message = 'yes'
        except Exception as e:
            message = 'no'
            # raise e

    m = {'message' : message }
    return render(request, 'createaccount.html', m)

def loginpage(request):
    message = ""
    page = ""
    if request.method == "POST":
        u = request.POST['iin']
        p = request.POST['password']

        user = authenticate(request, username=u, password = p)
        try:
            if user is not None:
                login(request, user)
                message = "no"
                g = request.user.groups.all()[0].name
                if g == 'Patient':
                    m = {'message' : message, 'page': page}
                    return render(request, 'patienthome.html', m)
                elif g =="Doctor":
                    m = {'message' : message, 'page': page}
                    return render(request, 'doctorhome.html', m)
            else:
                message = 'yes'
        except Exception as e:
            message = 'yes'
    return render(request, 'login.html')

def Logout(request):
	if not request.user.is_active:
		return redirect('loginpage')
	logout(request)
	return redirect('loginpage')

def adminlogin(request):
    return render(request, 'adminlogin.html')

def home(request):
    if not request.user.is_active:
        return redirect("loginpage")
    
    g = request.user.groups.all()[0].name
    if g == "Patient":
        return render(request, "patienthome.html")
    elif g == "Doctor":
        return render(request, "doctorhome.html")

def profile(request):
    if not request.user.is_active:
        return redirect('loginpage')
    g = request.user.groups.all()[0].name
    if g == 'Patient':
        patient_details = Patient.objects.all().filter(iin=request.user)
        d = { 'patient_details' : patient_details }
        return render(request,'patientprofile.html',d)
    if g == 'Doctor':
        doctor_details = Doctor.objects.all().filter(iin=request.user)
        d = { 'doctor_details' : doctor_details }
        return render(request,'doctorprofile.html',d)


def MakeAppointment(request):
    if not request.user.is_active:
        return redirect('loginpage')
    alldoctors = Doctor.objects.all()
    d = { 'alldoctors' : alldoctors }
    g = request.user.groups.all()[0].name
    if g == 'Patient':
        if request.method == 'POST':
            temp = request.POST['doctoremail']
            doctoremail = temp.split()[0]
            doctorname = temp.split()[1]
            patientname = request.POST['patientname']
            patientemail = request.POST['patientemail']
            appointmentdate = request.POST['appointmentdate']
            appointmenttime = request.POST['appointmenttime']
            symptoms = request.POST['symptoms']
            try:
                Appointment.objects.create(doctorname=doctorname, doctoremail=doctoremail,patientname=patientname, patientemail=patientemail,appointmentdate=appointmentdate,appointmenttime=appointmenttime,symptoms=symptoms,status=True,prescriptions="")
                error = "no"
            except:
                error = "yes"
            e = {"error": error }
            return render(request,'pateintmakeappointments.html', e)
	
        return render(request,'pateintmakeappointments.html',d)
    

def viewappointments(request):
    if not request.user.is_active:
        return redirect('loginpage')
    g = request.user.groups.all()[0].name
    if g == 'Patient':
        upcoming_appointment = Appointment.objects.filter(patientemail = request.user.email, appointmentdate__gte = timezone.now(), status = True).order_by('appointmentdate')
        previous_appointment = Appointment.objects.filter(patientemail = request.user.email, appointmentdate__lte = timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(patientemail = request.user.email, status = False).order_by('-appointmentdate')
        d = {'upcoming_appointment' : upcoming_appointment, "previous_appointment" :previous_appointment}
        return render(request, 'patientviewappointments.html', d)
    if g == 'Doctor':
        if request.method == "POST":
            prescriptiondata = request.POST['prescriptions']
            idvalue = request.POST['idofappointment']
            Appointment.objects.filter(id = idvalue).update(prescriptions  = prescriptiondata, status = False)
        upcoming_appointment = Appointment.objects.filter(doctoremail = request.user.email, appointmentdate__gte = timezone.now(), status = True).order_by('appointmentdate')
        previous_appointment = Appointment.objects.filter(doctoremail = request.user.email, appointmentdate__lt = timezone.now()).order_by('-appointmentdate') | Appointment.objects.filter(doctoremail = request.user, status = False).order_by('-appointmentdate')
        d = {'upcoming_appointment' : upcoming_appointment, "previous_appointment" :previous_appointment}
        return render(request, 'doctorviewappointment.html', d)
        