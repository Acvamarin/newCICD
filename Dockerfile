# Используем официальный Python образ
FROM python:3.9

# Устанавливаем рабочую директорию
WORKDIR /usr/src/app

# Копируем requirements.txt
COPY requirements.txt ./

# Устанавливаем зависимости
RUN pip install --no-cache-dir -r requirements.txt

# Копируем остальные файлы
COPY . .

# Экспонируем порт
EXPOSE 5000

# Запускаем приложение
CMD ["python", "app.py"]
