# Generated by Django 3.0.2 on 2020-01-20 00:49

from django.db import migrations, models
import django.db.models.deletion
import django_extensions.db.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Company',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('code', models.IntegerField(unique=True, verbose_name='업체코드')),
                ('name', models.CharField(max_length=45, verbose_name='업체명')),
                ('address', models.CharField(max_length=512, verbose_name='주소')),
                ('phone_number', models.CharField(max_length=45, verbose_name='전화번호')),
                ('fax_number', models.CharField(max_length=45, verbose_name='팩스번호')),
                ('business_type', models.CharField(max_length=45, verbose_name='업종')),
                ('main_product', models.CharField(max_length=45, verbose_name='주생산물')),
                ('type', models.CharField(max_length=45, verbose_name='기업규모')),
                ('research_field', models.CharField(max_length=45, verbose_name='연구분야')),
                ('department', models.CharField(max_length=45, verbose_name='지방청')),
            ],
            options={
                'db_table': 'company',
            },
        ),
        migrations.CreateModel(
            name='EmploymentHistory',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', django_extensions.db.fields.CreationDateTimeField(auto_now_add=True, verbose_name='created')),
                ('modified', django_extensions.db.fields.ModificationDateTimeField(auto_now=True, verbose_name='modified')),
                ('active_duty_assign_count', models.IntegerField(verbose_name='현역 배정 인원')),
                ('active_duty_transfer_count', models.IntegerField(verbose_name='현역 편입 인원')),
                ('active_duty_in_service_count', models.IntegerField(verbose_name='현역 복무 인원')),
                ('supplement_duty_assign_count', models.IntegerField(verbose_name='보충역 배정 인원')),
                ('supplement_duty_transfer_count', models.IntegerField(verbose_name='보충역 편입 인원')),
                ('supplement_duty_in_service_count', models.IntegerField(verbose_name='보충역 복무 인원')),
                ('recruitment_status', models.CharField(max_length=45, verbose_name='채용유무')),
                ('company', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='company.Company')),
            ],
            options={
                'db_table': 'employment_history',
            },
        ),
    ]
