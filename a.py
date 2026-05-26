import os
import json

# Укажи имя папки с картинками
folder_name = 'images'

# Получаем список всех файлов с расширениями картинок
extensions = ('.jpg', '.jpeg', '.png', '.webp', '.gif', '.heic')
photo_list = [f"{folder_name}/{f}" for f in os.listdir(folder_name) if f.lower().endswith(extensions)]

# Выводим в консоль готовый массив для вставки в JavaScript
print(json.dumps(photo_list, indent=4))