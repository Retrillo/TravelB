import json
from django.core import serializers
import os
import django

# Подключаем Django
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "TravelB.settings")  # замени на путь к твоему settings
django.setup()

# Экспорт всех данных всех моделей
from django.apps import apps

all_models = apps.get_models()
all_objects = []

for model in all_models:
    qs = model.objects.all()
    all_objects.extend(list(qs))

# Сериализация в JSON
data = serializers.serialize("json", all_objects, indent=2)

with open("db_dump_utf8.json", "w", encoding="utf-8") as f:
    f.write(data)

print("Экспорт завершён: db_dump_utf8.json")
