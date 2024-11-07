# Базовый образ
FROM python:3.10

# Устанавливаем рабочую директорию
WORKDIR /app

# Обновляем pip
RUN pip install --upgrade pip

# Копируем файлы и устанавливаем зависимости
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Копируем проект в контейнер
COPY . /app/

# Запускаем сервер
CMD ["sh", "-c", "python language_bot_api/manage.py migrate && python language_bot_api/manage.py runserver 0.0.0.0:8000"]
