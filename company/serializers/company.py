from rest_framework import serializers

from company.models import Company


class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model = Company
        fields = (
            'id',
            'code',
            'name',
            'address',
            'phone_number',
            'fax_number',
            'business_type',
            'main_product',
            'type',
            'research_field',
            'department',
            'selection_year',
        )
