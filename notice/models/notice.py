from model_utils.models import TimeStampedModel

from django.db import models


class Notice(TimeStampedModel):
    serial_number = models.CharField(max_length=20, db_index=True)

    title = models.CharField(max_length=100)
    writer = models.CharField(max_length=20)
    date = models.DateField()
    content = models.TextField()

    def __str__(self):
        return "%s (%s, %s)" % (self.title, self.writer, self.date.strftime("%Y-%m-%d"))

    class Meta:
        db_table = 'notice'
