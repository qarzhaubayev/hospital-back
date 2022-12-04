from django.shortcuts import render, redirect
from accounts.models import *
from django.contrib.auth.models import User, Group

def homepage(request):
    return render(request, 'index.html')

def aboutpage(request):
    return render(request, 'about.html')

def loginpage(request):
    return render(request, 'login.html')

def createaccountpage(request):
    user = 'none'
    if request.method == 'POST':
        iin = request.POST['iin']
        name = request.POST['name']
        surname = request.POST['surname']
        midname = request.POST['midname']
        password = request.POST['password']
        repeatpassword = request.POST['repeatpassword']
        # iin = request.POST['iin']
        email = request.POST['email']
        gender = request.POST['gender']
        birthday_date = request.POST['birthday_date']
        contact_number = request.POST['contact_number']
        emergency_contact_number = request.POST['emergency_contact_number']
        address = request.POST['address']
        blood_type = request.POST['blood_type']
        marital_status = request.POST['marital_status']
        
    
        try:
            if (password == repeatpassword):
                Patient.objects.create(name = name, surname = surname, midname = midname, gender = gender, birthday_date = birthday_date, contact_number=contact_number, emergency_contact_number = emergency_contact_number, email = email,  address = address, blood_type = blood_type, marital_status = marital_status)
                user = User.objects.create_user(iin_num=iin, password=password, email= email, username= iin)
                pat_group = Group.objects.get(name='Patient')
                pat_group.user_set.add(user)
                user.save()
                message = 'Successfully'
            else:
                message = 'Failed'
        except Exception as e:
            raise e
            message = 'Failed'
        m = {'message': message }
    return render(request, 'createaccount.html', m)

def login_admin(request):
    return render(request, 'adminlogin.html')