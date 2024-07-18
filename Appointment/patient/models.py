from django.db import models


class Doctor(models.Model):
    doctor_name = models.CharField(max_length=100)
    doctor_email = models.EmailField()
    doctor_Birthdate = models.DateField()
    doctor_phone = models.CharField(max_length=15)
    speciality = models.CharField(max_length=100)
    doctor_address = models.TextField()
    doctor_join_date = models.DateField()

    GENDER_CHOICES = [
        ("M", "Male"),
        ("F", "Female"),
        ("O", "Other"),
    ]

    NATIONALITY_CHOICES = [
        ("IN", "Indian"),
        ("US", "American"),
        ("UK", "British"),
    ]

    doctor_gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    doctor_nationality = models.CharField(max_length=2, choices=NATIONALITY_CHOICES)

    def __str__(self):
        return self.doctor_name


class Appointment(models.Model):
    name = models.ForeignKey(Doctor, on_delete=models.CASCADE)
    app_date = models.DateField(blank=False, auto_now_add=False)
    token_no = models.IntegerField()
    status = models.BooleanField(default=False)

    def __str__(self):
        return self.name.doctor_name
