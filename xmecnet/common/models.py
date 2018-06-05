from django.db import models


class User(models.Model):
    username = models.CharField(max_length=50, primary_key=True)
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
        return '<{0}>'.format(self.username)

    class Meta:
        verbose_name_plural = 'Users'
        ordering = ['username']
