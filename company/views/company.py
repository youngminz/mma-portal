from rest_framework.viewsets import ReadOnlyModelViewSet

from company.models import Company
from company.serializers.company import CompanySerializer


class CompanyViewSet(ReadOnlyModelViewSet):
    queryset = Company.objects.all()
    serializer_class = CompanySerializer
