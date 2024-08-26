FROM python:3.10

# Встановимо змінну середовища
ENV APP_HOME /app

# Встановимо робочу директорію всередині контейнера
WORKDIR $APP_HOME

# Скопіюємо файли застосунку в робочу директорію контейнера
COPY Pipfile Pipfile.lock ./
COPY . .

# Встановимо залежності всередині контейнера
RUN pip install pipenv && pipenv install --deploy --ignore-pipfile

# Використовуємо CMD для запуску програми. Не вказуємо `python main.py` тут.
CMD ["python", "main.py"]