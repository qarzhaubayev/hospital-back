from django.db import models

# Create your models here.
from django.db import models
from django.contrib.auth.models import BaseUserManager, PermissionsMixin
from account.models import User

class AccountManager(BaseUserManager):
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
            schedule=schedule, appointment_duration=appointment_duration, price=price,
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
                        schedule, appointment_duration, price, specialize,
                        contact_number, experience,
                        address, password, **extra_fields):
        return self._create_doctor(self, name, surname, midname,
                        birthday_date, iin_num, id,
                        education, departament_id, category, photo,
                        schedule, appointment_duration, price, specialize,
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
    objects=AccountManager()

