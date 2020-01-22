from model_utils.models import TimeStampedModel

from django.db import models


class Attachment(TimeStampedModel):
    notice = models.ForeignKey('notice.Notice', on_delete=models.CASCADE)
    serial_number = models.CharField(max_length=20)

    file = models.FileField(null=True)
    file_name = models.CharField(max_length=100)

    def __str__(self):
        return self.file_name

    class Meta:
        db_table = 'attachment'
