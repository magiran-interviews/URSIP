from URSIP.apps.db.models import Essence, Organization
from django.core.management.base import BaseCommand
import pandas as pd
from pandas.core.frame import DataFrame
from datetime import date


IMPORT_FILE_PATH = "URSIP/apps/import_data/data/example.xlsx"
IMPORT_FILE_SHEET = "Лист1"
IMPORT_FILE_COLUMNS = [
    "external_id", 
    "organization_name", 
    "fact_qliq_data1", 
    "fact_qliq_data2", 
    "fact_qoil_data1", 
    "fact_qoil_data2", 
    "forecast_qliq_data1", 
    "forecast_qliq_data2", 
    "forecast_qoil_data1", 
    "forecast_qoil_data2"
]


def date_generator() -> date:
    for day_num in range(1, 32):
        yield date(2023, 3, day_num)


def read_excel() -> DataFrame:
    return pd.read_excel(IMPORT_FILE_PATH, IMPORT_FILE_SHEET, names=IMPORT_FILE_COLUMNS, skiprows=[0, 1])


def create_essences(essences: DataFrame) -> list[Essence]:
    date_gen = date_generator()

    cur_organizations_names = essences.get("organization_name").unique()
    cur_organizations = Organization.objects.filter(name__in=cur_organizations_names)

    essences_data = [dict(row[1]) for row in essences.iterrows()]
    for essence in essences_data:
        essence["organization_id"] = cur_organizations.get(name=essence["organization_name"]).pk
        essence["date_at"] = next(date_gen)
        del essence["organization_name"]

    essences = [Essence(**essence) for essence in essences_data]
    return Essence.objects.bulk_create(essences)


class Command(BaseCommand):
    def handle(self, *args: tuple, **options: dict) -> None:
        essences_df = read_excel()
        essences = create_essences(essences_df)
        print(f"Импортированно {len(essences)} элементов.")
