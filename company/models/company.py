from django_extensions.db.models import TimeStampedModel
from django.db import models


class Company(TimeStampedModel):
    code = models.IntegerField("업체코드", unique=True)
    name = models.CharField("업체명", max_length=45)
    address = models.CharField("주소", max_length=512)
    phone_number = models.CharField("전화번호", max_length=45)
    fax_number = models.CharField("팩스번호", max_length=45)
    business_type = models.CharField("업종", max_length=45)
    main_product = models.CharField("주생산물", max_length=45)
    type = models.CharField("기업규모", max_length=45)
    research_field = models.CharField("연구분야", max_length=45)
    department = models.CharField("지방청", max_length=45)

