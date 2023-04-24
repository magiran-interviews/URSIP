# Заметки о выполнении задания

## Как устроено решение

- 2 приложения django: db, import_data.
- В приложении db 2 модели: Organization, Essence (сущность). В Essence импортируются данные из excel.
- В приложении db 2-ая миграция - это кастомная миграция для создания организаций, которые присутствуют в файле для импорта.
- После миграции можно вручную запускать импорт данных их excel. Реализовал импорт через пользовательскую команду django-admin.
- Группировка полей Qliq и Qoil сделана в методе total модели Essence. При помощи total можно получить сгруппированный по дням результат за всё время либо по заданному интервалу дат.

## Установка проекта

1. Активировать виртуальное окружение

1. Установить зависимости
    ```bash
    pip install -r requirements.txt
    ```

1. Сделать миграции
    ```bash
    ./manage.py migrate
    ```


## Импорт данных из excel

Файл excel для импорта: `"URSIP/apps/import_data/data/example.xlsx"`

Код импорта: `"URSIP/apps/import_data/management/commands/import_excel.py"`

Запуск импорта:
```bash
./manage.py import_excel
```

## Примеры расчета тотал по Qoil, Qliq

Файл с примерами: `"URSIP/apps/import_data/management/commands/total_examples.py"`.

Запуск файла
```bash
./manage.py total_examples
```
