# Core
from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import PermissionsMixin

# Managers
from .managers.user_manager import EmployeeUserManager
from .managers.time_record_manager import TimeRecordManager


class Employee(AbstractBaseUser, PermissionsMixin):
    """
    Employee model
    """

    ROLE_CHOICES = (
        ('D', 'Director'),
        ('E', 'Employee'),
        ('O', 'Owner'),
        ('QA', 'Quality Analyst'),
        ('S', 'Supervisor'),
        ('TL', 'Team Leader'),
    )

    employee_id = models.IntegerField(null=True, blank=True)
    email = models.EmailField(unique=True)
    username = models.CharField(max_length=32)
    first_name = models.CharField(max_length=32, blank=True)
    maiden_name = models.CharField(max_length=32, blank=True)
    last_name = models.CharField(max_length=32, blank=True)
    nickname = models.CharField(max_length=32, blank=True)
    role = models.CharField(max_length=3, choices=ROLE_CHOICES)
    date_tenure = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=True)
    avatar = models.ImageField(upload_to='employees/', null=True, blank=True)

    objects = EmployeeUserManager()

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []

    class Meta:
        db_table = "employee"

    def __str__(self):
        return str(self.employee_id) + ': %s %s' % (self.first_name, self.last_name)


class TimeRecord(models.Model):
    """
    Time record model
    """

    TIME_OF_SHIFT_CHOICES = (
        ('6AM - 5PM', '6AM - 5PM'),
        ('8AM - 7PM', '8AM - 7PM'),
        ('7PM - 6AM', '7PM - 6AM'),
        ('9PM - 8AM', '9PM - 8AM'),
    )

    employee = models.ForeignKey(
        Employee,
        on_delete=models.CASCADE,
        related_name='time_record_employee')
    employee_name = models.CharField(max_length=32)
    time_of_shift = models.CharField(max_length=32, choices=TIME_OF_SHIFT_CHOICES)
    date_of_shift = models.DateField(auto_now_add=True)
    timestamp_in = models.DateTimeField(auto_now_add=True)
    timestamp_out = models.DateTimeField()

    objects = TimeRecordManager()

    class Meta:
        db_table = "time_record"

    def __str__(self):
        return str(self.employee_name) + ': ' + str(self.timestamp_in) + ' - ' + str(self.timestamp_out)
