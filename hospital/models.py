from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin
from django.core.validators import MaxValueValidator, MinValueValidator



# Create your models here.


class UserCreation(BaseUserManager):
    def _create_user(self, iin_num, password, is_superuser, is_staff, **extra_fields):
        if not iin_num:
            raise ValueError('The given iin_num must be set')
        user = self.model(iin_num=iin_num, is_superuser=is_superuser, is_staff=is_staff, is_active=True, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, iin_num, password=None, **extra_fields):
        return self._create_user(iin_num, password, False, False, **extra_fields)

    def create_superuser(self, iin_num, password, **extra_fields):
        return self._create_user(iin_num, password, True, True, **extra_fields)

class User(AbstractBaseUser, PermissionsMixin):
    # any fields you would like to add
    join_date = models.DateTimeField(auto_now_add=True)
    last_login_date  = models.DateTimeField(null=True)
    is_active   = models.BooleanField(default=True)
    is_staff    = models.BooleanField(default=False)
    iin_number         = models.CharField(max_length=12, primary_key=True)

    USERNAME_FIELD = 'iin_num'
    REQUIRED_FIELDS = []

    objects = UserCreation()


departments=[('Surgery','Surgery'),
('Dermatologists','Dermatologists'),
('Gynecology', 'Gynecology'),
('Obstetrics', 'Obstetrics'),
('Emergency Medicine Specialists','Emergency Medicine Specialists'),
('Allergists/Immunologists','Allergists/Immunologists'),
('Anesthesiologists','Anesthesiologists'),
('Colon and Rectal Surgeons','Colon and Rectal Surgeons')
]

class DoctorAccount(BaseUserManager):
    def _create_doctor(self, name, surname, middlename,
                    date_of_birth, iin_num, id_num,
                    degree_of_ed, department_id, specialization_id, category, photo, schedule, app_duration, price_of_appoint,
                    contacts, exp,
                    address, password, **extra_fields):
        values = [name, surname, middlename, date_of_birth, id_num, degree_of_ed, department_id, specialization_id, category, photo,
                    schedule, app_duration, price_of_appoint, contacts, exp, address, password]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        user = self.model(
            name=name, surname=surname, middlename=middlename,
            date_of_birth=date_of_birth, iin_num=iin_num, id_num=id_num,
            degree_of_ed=degree_of_ed, department_id=department_id, specialization_id=specialization_id, category=category, photo=photo,
            schedule=schedule, app_duration=app_duration, price_of_appoint=price_of_appoint,
            contacts=contacts, exp=exp,
            address=address,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_doctor(self, name, surname, middlename,
                        date_of_birth, iin_num, id_num,
                        degree_of_ed, department_id, category, photo,
                        schedule, app_duration, price_of_appoint, specialization_id,
                        contacts, exp,
                        address, password, **extra_fields):
        return self._create_doctor(self, name, surname, middlename,
                        date_of_birth, iin_num, id_num,
                        degree_of_ed, department_id, category, photo,
                        schedule, app_duration, price_of_appoint, specialization_id,
                        contacts, exp,
                        address, password, **extra_fields)


class Doctor(models.Model):
    name =  models.CharField(max_length = 200, null = True)
    surname =  models.CharField(max_length = 200, null = True)
    middlename =  models.CharField(max_length = 200, null = True)
    date_of_birth =  models.DateField(max_length = 200, null = True)
    id_num =  models.IntegerField(null=True)
    degree_of_education =  models.CharField(max_length = 200, null = True)
    department_id  =  models.IntegerField(null = True)
    specialization_details_ID  =  models.IntegerField(null = True)
    category  =  models.CharField(max_length = 200, null = True)
    photo = models.FileField(upload_to='images/', null= True)
    # schedule  =  models.CharField(max_length = 200, null = True)
    schedule = models.JSONField(default=list)
    app_duration = models.IntegerField(max_length=5)
    price_of_appointment  =  models.IntegerField(validators = [MaxValueValidator(99999), MinValueValidator(1000)], null= True)
    contacts = models.IntegerField(max_length=12)
    exp = models.CharField(max_length= 3)
    homepage_URL =  models.CharField(null=True)
    address =  models.CharField(max_length = 200, null = True)
    
    USERNAME_FIELD = 'iin_num'
    REQUIRED_FIELD = ["name", "surname", "middlename", "date_of_birth", "id_num", "degree_of_ed", "department_id", "specialization_id", "category", "photo", "schedule", "app_duration", "price_of_appoint", "contacts", "exp", "address", "password"]
    object = UserCreation()



# Creation of patients




class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null= True)
# NEED TO DELETE NULL VALUES EXCEPT EMAIL (AS EMAIL OPTIONAL)
    name =  models.CharField(max_length = 50, null = True)
    surname =  models.CharField(max_length = 200, null = True)
    middlename =  models.CharField(max_length = 200, null = True)
    date_of_birth =  models.DateField(max_length = 200, null = True)
    iin_num =  models.IntegerField(null = True)
    id_number =  models.IntegerField(null = True)
    emergancy_contact_number =  models.IntegerField(null = True)
    phone_num =  models.IntegerField(null = True)
    email =  models.EmailField(max_length = 200, null = True)
    address =  models.CharField(max_length = 40, null = True)
    marital_status =  models.CharField(max_length = 200, null = True)
    registration_date = models.DateTimeField(auto_now_add = True)
    
    USERNAME_field = "iin_number"
    required_f = ["","",""]
    