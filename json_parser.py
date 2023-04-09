import json
from datetime import datetime


def set_updated_fields_to_current_datetime(data: dict | list, field_name: str = "updated") -> None:
    """
    Рекусрсивная функция для поиска поля "updated" и замены его значения на таймстемп в ISO 8601 формате
    """
    if isinstance(data, dict):
        for key, value in data.items():
            if key == field_name:
                data[key] = datetime.now().isoformat()
            elif isinstance(value, (dict, list)):
                set_updated_fields_to_current_datetime(value, field_name)
    elif isinstance(data, list):
        for item in data:
            set_updated_fields_to_current_datetime(item, field_name)


# Открываем файл, в котором необходимо поменять дату
with open('example.json', 'r') as f:
    file_data = json.load(f)

# Применяем функцию к файлу
set_updated_fields_to_current_datetime(file_data)

# Записываем изменённые данные в тот же файл
with open('example.json', 'w') as f:
    json.dump(file_data, f, indent=4)
