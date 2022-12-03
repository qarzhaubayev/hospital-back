from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager, PermissionsMixin

# Create your models here.
class UserManager(BaseUserManager):
    use_in_migrations = True
    def _create_user(self, iin_num, password, is_superuser, is_staff, **extra_fields):
        if not iin_num:
            raise ValueError('The given iin must be set')
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
    is_staff    = models.BooleanField(default=False)
    is_active   = models.BooleanField(default=True)
    iin_num         = models.CharField(max_length=12, primary_key=True)

    USERNAME_FIELD = 'iin_num'
    REQUIRED_FIELDS = []

    objects = UserManager()



class DoctorManager(BaseUserManager):
    use_in_migrations = True

    def _create_doctor(self, name, surname, midname, birthday_date, iin_num, id, education, departament_id, specialize, category, photo, schedule, appointment_duration, price, contact_number, experience, address, password, **extra_fields):
        values = [name, surname, midname, birthday_date, id, education, departament_id, specialize, category, photo,
                  schedule, appointment_duration, price, contact_number, experience, address, password]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        user = self.model(
            name=name, surname=surname, midname=midname,
            birthday_date=birthday_date, iin_num=iin_num, id=id,
            education=education, departament_id=departament_id, specialize=specialize, category=category, photo=photo,
            # schedule=schedule, 
            appointment_duration=appointment_duration, price=price,
            contact_number=contact_number, experience=experience,
            address=address,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_doctor(self, name, surname, midname,
                        birthday_date, iin_num, id,
                        education, departament_id, category, photo,
                        # schedule, 
                        appointment_duration, price, specialize,
                        contact_number, experience,
                        address, password, **extra_fields):
        return self._create_doctor(self, name, surname, midname,
                        birthday_date, iin_num, id,
                        education, departament_id, category, photo,
                        # schedule, 
                        appointment_duration, price, specialize,
                        contact_number, experience,
                        address, password, **extra_fields)

class Doctor(User):
    use_in_migrations = True
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    midname = models.CharField(max_length=200)
    birthday_date = models.CharField(max_length=10)
    id = models.CharField(max_length=12)
    education = models.CharField(max_length=3)
    departament_id = models.CharField(max_length=200)
    specialize = models.CharField(max_length=200)
    category = models.CharField(max_length=200)
    photo = models.FileField(upload_to='images/')
    schedule = models.JSONField(default=list)
    appointment_duration = models.CharField(max_length=5)
    price = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=12)
    experience = models.CharField(max_length=3)
    url = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200)

    USERNAME_FIELD = "iin_num"
    REQUIRED_FIELD = ["name", "surname", "midname", "birthday_date", "id", "education", "departament_id", "specialize", "category", "photo", "schedule", "appointment_duration", "price", "contact_number", "experience", "address", "password"]
    objects=DoctorManager()



class PatientManager(BaseUserManager):
    use_in_migrations = True

    def _create_patient(self, name, surname, midname,
                        birthday_date, iin_num, id,
                        blood_type, marital_status,
                        contact_number, emergency_contact_number,
                        address, password, **extra_fields):
        values = [name, surname, midname, birthday_date, iin_num, id, blood_type, marital_status, contact_number, emergency_contact_number, address, password]
        field_value_map = dict(zip(self.model.REQUIRED_FIELDS, values))
        for field_name, value in field_value_map.items():
            if not value:
                raise ValueError('The {} value must be set'.format(field_name))

        user = self.model(
            name=name, surname=surname, midname=midname,
            birthday_date=birthday_date, iin_num=iin_num, id=id,
            blood_type=blood_type, marital_status=marital_status,
            contact_number=contact_number, emergency_contact_number=emergency_contact_number,
            address=address,
            **extra_fields
        )
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_patient(self, name, surname, midname,
                        birthday_date, iin_num, id,
                        blood_type, marital_status,
                        contact_number, emergency_contact_number,
                        address, password, **extra_fields):
        #extra_fields.setdefault('is_staff', False)
        #extra_fields.setdefault('is_superuser', False)
        return self._create_patient(self, name, surname, midname,
                                    birthday_date, iin_num, id,
                                    blood_type, marital_status,
                                    contact_number, emergency_contact_number,
                                    address, password, **extra_fields)

class Patient(User):
    use_in_migrations = True
    name = models.CharField(max_length=200)
    surname = models.CharField(max_length=200)
    midname = models.CharField(max_length=200)
    birthday_date = models.CharField(max_length=10)
    #iin_num = models.CharField(max_length=12, primary_key=True)
    id = models.CharField(max_length=12)
    blood_type = models.CharField(max_length=3)
    marital_status = models.CharField(max_length=8)
    contact_number = models.CharField(max_length=12)
    emergency_contact_number = models.CharField(max_length=12)
    email = models.CharField(max_length=200, blank=True)
    address = models.CharField(max_length=200)

    USERNAME_FIELD = "iin_num"
    REQUIRED_FIELD = ["name", "surname", "midname", "birthday_date", "id", "blood_type", "marital_status", "contact_number", "emergency_contact_number", "address", "password"]
    objects=PatientManager()

