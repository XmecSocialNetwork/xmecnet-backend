from django.db import models
from django.contrib.auth.hashers import make_password, check_password

import datetime

class User(models.Model):
    email = models.EmailField(max_length=100, primary_key=True)
    name = models.CharField(max_length=60)
    password = models.CharField(max_length=255)
    roll_no = models.CharField(max_length=15, blank=True, null=True)
    date_of_birth = models.DateField()

    BRANCH_CHOICES = (
            ('CS', 'Computer Science and Engineering'),
            ('BME', 'Biomedical Engineering'),
            ('EC', 'Electronics & Communication Engineering'),
            ('EEE', 'Electrical Engineering'),
        )

    branch = models.CharField(max_length=3, choices=BRANCH_CHOICES,
                              blank=True, null=True)

    def __str__(self):
        return '<{0} {1}>'.format(self.name, self.email)

    class Meta:
        verbose_name_plural = 'Users'
        ordering = ['name']


    @classmethod
    def create(cls, email, name, password, dobday, dobmonth, dobyear, branch, roll_no=None):
        try:
            dob = datetime.date(year=dobyear, month=dobmonth, day=dobday)
            x = cls(email=email,
                    name=name,
                    #password=make_password(password),
                    password=password,
                    roll_no=roll_no,
                    date_of_birth=dob,
                    branch=branch
                   )
            x.save()

        except Exception as e:
            print(e)

    @classmethod
    def login(cls, email, password):
        try:
            x = cls.objects.get(email=email)
            print (password)
            if check_password(password,x.password):
                return x
            else:
                return False

        except Exception as e:
            print(e)
