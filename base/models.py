from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm

MARITAL_GROUP = (
('s', 'Single'),
('m', 'Married'),
('w', 'Widowed'),
('d', 'Divorsed')
)

CATEGORY_GROUP = (
    ('j', 'Junior'),
    ('m', 'Middle'),
    ('s', 'Senior')
)

DEGREE_GROUP = (
    ('b', 'BS'),
    ('m', 'MD'),
    ('p', 'PhD')
)

BLOOD_GROUPS = (
    ('A', 'A'),
    ('B', 'B'),
    ('AB', 'AB'),
    ('O', 'O')
)

class Doctor(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)
    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    birth_date = models.DateField("Birth Date", default="2000-01-01", blank=False, null=False)
    iin_number = models.CharField(max_length=12, blank=False, null=False)
    id_number = models.CharField(max_length=12, blank=False, null=False)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    department_id = models.CharField(max_length=11, blank=True, null=True)
    specialization_id = models.CharField(max_length=11, blank=True, null=True)
    experience_in_years = models.CharField(max_length=12, blank=False, null=False)
    photo = models.ImageField(blank=False, null=False)
    category = models.CharField(max_length=20, choices=CATEGORY_GROUP, default=None, blank=False, null=False)
    appointment_price = models.CharField(max_length=6, blank=False, null=False)
    shedule_details = models.CharField(max_length=500, blank=True, null=True)
    degree = models.CharField(max_length=20, choices=DEGREE_GROUP, default=None, blank=False, null=False)
    rating = models.CharField(max_length=2, blank=False, null=False)
    address = models.CharField(max_length=150, blank=False, null=False)
    homepage_url = models.URLField(blank=True, null=True)


    def __str__(self):
        return f"{self.first_name} {self.surname}"
    

class Patient(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, primary_key=True, unique=True)
    first_name = models.CharField(max_length=150)
    surname = models.CharField(max_length=150)
    middle_name = models.CharField(max_length=150)
    birth_date = models.DateField("Birth Date", default="2000-01-01", blank=False, null=False)
    blood_group = models.CharField(max_length=10, choices=BLOOD_GROUPS, default=None, blank=False, null=False)
    iin_number = models.CharField(max_length=12, blank=False, null=False)
    id_number = models.CharField(max_length=12, blank=False, null=False)
    phone_number = models.CharField(max_length=11, blank=True, null=True)
    emergency_phone_number = models.CharField(max_length=11, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    address = models.CharField(max_length=150, blank=False, null=False)
    marital_status = models.CharField(max_length=20, choices=MARITAL_GROUP, default=None, blank=False, null=False)
    registration_date = models.DateTimeField(auto_now_add=True)
    modified_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.first_name} {self.surname}"
