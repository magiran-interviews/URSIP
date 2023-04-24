from django.core.management.base import BaseCommand
from django.db.models import Sum
from URSIP.apps.db.models import Essence
from datetime import date


class Command(BaseCommand):
    def handle(self, *args: tuple, **options: dict) -> None:
        print("Кол-во строк в таблице:", Essence.total().count())

        print(
            "Первая дата интервала    2023-03-12/2023-03-15:", 
            Essence.total(start=date(2023, 3, 12), end=date(2023, 3, 15)).first()["date_at"].isoformat()
        )
        print(
            "Последняя дата интервала 2023-03-12/2023-03-15:", 
            Essence.total(start=date(2023, 3, 12), end=date(2023, 3, 15)).last()["date_at"].isoformat()
        )

        print(
            "Общая сумма fact_qliq_data1 с 10 марта 2023 включительно:",
            Essence.total(start=date(2023, 3, 10)).aggregate(
                sum_total_fact_qliq_data1=Sum("total_fact_qliq_data1")
            )["sum_total_fact_qliq_data1"]
        )
