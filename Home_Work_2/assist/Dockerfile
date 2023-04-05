# Docker-команда FROM указывает базовый образ контейнера
# Наш базовый образ - это Linux с предустановленным python-3.10
FROM python:3.10

# Установим переменную окружения
ENV APP_HOME /app

# Установим рабочую директорию внутри контейнера
WORKDIR $APP_HOME

# Скопируем остальные файлы в рабочую директорию контейнера
COPY Dockerfile requirements.txt /app/
COPY assist /app/assist

ENV PYTHONPATH "${PYTHONPATH}:/app/assist"

# Установим зависимости внутри контейнера
RUN pip install -r requirements.txt
RUN ls -la
# Запустим наше приложение внутри контейнера
CMD ["python", "assist/interface.py"]