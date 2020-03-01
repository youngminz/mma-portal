from django.db import models
from django_extensions.db.models import TimeStampedModel


class EmploymentHistory(TimeStampedModel):
    company = models.ForeignKey('company.Company', models.CASCADE)

    active_duty_assign_count = models.IntegerField('현역 배정 인원')
    active_duty_transfer_count = models.IntegerField('현역 편입 인원')
    active_duty_in_service_count = models.IntegerField('현역 복무 인원')

    supplement_duty_assign_count = models.IntegerField('보충역 배정 인원')
    supplement_duty_transfer_count = models.IntegerField('보충역 편입 인원')
    supplement_duty_in_service_count = models.IntegerField('보충역 복무 인원')

    recruitment_status = models.CharField('채용유무', max_length=45)

    class Meta:
        db_table = 'employment_history'
