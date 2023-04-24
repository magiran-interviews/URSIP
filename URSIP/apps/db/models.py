from django.db.models import (
    Model, 
    IntegerField, 
    PositiveIntegerField, 
    CharField, 
    DateField, 
    ForeignKey, 
    CASCADE, 
    Sum, 
    QuerySet,
)
from datetime import date


class Organization(Model):
    name = CharField(verbose_name="Наименование организации", max_length=128, unique=True)


class Essence(Model):
    external_id = PositiveIntegerField(verbose_name="Внешний ID")
    organization = ForeignKey(Organization, CASCADE)
    fact_qliq_data1 = IntegerField(verbose_name="Фактический qliq_data1")
    fact_qliq_data2 = IntegerField(verbose_name="Фактический qliq_data2")
    fact_qoil_data1 = IntegerField(verbose_name="Фактический qoil_data1")
    fact_qoil_data2 = IntegerField(verbose_name="Фактический qoil_data2")
    forecast_qliq_data1 = IntegerField(verbose_name="Планируемый qliq_data1")
    forecast_qliq_data2 = IntegerField(verbose_name="Планируемый qliq_data2")
    forecast_qoil_data1 = IntegerField(verbose_name="Планируемый qoil_data1")
    forecast_qoil_data2 = IntegerField(verbose_name="Планируемый qoil_data2")
    date_at = DateField(verbose_name="Дата")

    @classmethod
    def total(cls, start: date=date(1, 1, 1), end: date=date(9999, 12, 31)) -> QuerySet:
        return cls.objects.filter(date_at__gte=start, date_at__lte=end).values("date_at").annotate(
            total_fact_qliq_data1=Sum('fact_qliq_data1'),
            total_fact_qliq_data2=Sum('fact_qliq_data2'),
            total_fact_qoil_data1=Sum('fact_qoil_data1'),
            total_fact_qoil_data2=Sum('fact_qoil_data2'),
            total_forecast_qliq_data1=Sum('forecast_qliq_data1'),
            total_forecast_qliq_data2=Sum('forecast_qliq_data2'),
            total_forecast_qoil_data1=Sum('forecast_qoil_data1'),
            total_forecast_qoil_data2=Sum('forecast_qoil_data2'),
        ).order_by("date_at")
