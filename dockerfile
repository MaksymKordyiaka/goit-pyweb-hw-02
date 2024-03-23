# Використовуйте офіційний образ Python як базовий
FROM python:3.11.3-slim

# Встановіть poetry
RUN pip install poetry

# Створіть директорію для вашого проекту
WORKDIR /usr/src/app

# Копіюйте файли pyproject.toml та poetry.lock у контейнер
COPY pyproject.toml poetry.lock ./

# Встановіть залежності проекту
RUN poetry install --no-root

# Копіюйте ваш код проекту у контейнер
COPY . .

# Вкажіть команду для запуску вашого проекту
CMD ["python", "main.py"]