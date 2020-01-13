# Core
from django.db import models


class TimeRecordQueryset(models.query.QuerySet):
    """
    Time record queryset
    """

    def get_all(self):
        return self.all()

    def find_by_id(self, id):
        from ..models import TimeRecord

        try:
            return self.get(id=id)
        except TimeRecord.DoesNotExist:
            return 'Time record not found'

    def find_by_employee(self, employee):
        from ..models import TimeRecord

        try:
            return self.get(employee=employee)
        except TimeRecord.DoesNotExist:
            return 'Time record not found'

    def filter_by_time_of_shift(self, time_of_shift):
        return self.filter(time_of_shift=time_of_shift)
    
    def filter_by_date_of_shift(self, date_of_shift):
        return self.filter(date_of_shift=date_of_shift)


class TimeRecordManager(models.Manager):
    """
    Time record manager
    """

    def get_queryset(self):
        return TimeRecordQueryset(self.model, using=self._db)

    def get_all(self):
        return self.get_queryset().get_all()

    def find_by_id(self, id):
        return self.get_queryset().find_by_id(id)

    def find_by_employee(self, employee):
        return self.get_queryset().find_by_employee(employee)

    def filter_by_time_of_shift(self, time_of_shift):
        return self.get_queryset().filter_by_time_of_shift(time_of_shift)

    def filter_by_date_of_shift(self, date_of_shift):
        return self.get_queryset().filter_by_date_of_shift(date_of_shift)
