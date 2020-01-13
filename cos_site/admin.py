# Core
from django.contrib import admin
from .models import Employee, TimeRecord


class EmployeeAdmin(admin.ModelAdmin):
    """
    Employee admin
    """

    list_filter = (
        'role',
        'is_active',
        'is_staff',
    )
    list_display = (
        'employee_id',
        'email',
        'username',
        'first_name',
        'maiden_name',
        'last_name',
        'nickname',
        'role',
        'date_tenure',
        'is_active',
        'is_staff',
    )


class TimeRecordAdmin(admin.ModelAdmin):
    """
    Time record admin
    """

    list_filter = (
        'employee',
        'time_of_shift',
    )
    list_display = (
        'employee',
        'employee_name',
        'time_of_shift',
        'date_of_shift',
        'timestamp_in',
        'timestamp_out',
    )


admin.site.register(Employee, EmployeeAdmin)
admin.site.register(TimeRecord, TimeRecordAdmin)
