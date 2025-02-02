
# Expense Tracker

## Описание

Expense Tracker — это приложение для отслеживания расходов. Оно позволяет пользователю добавлять, редактировать и удалять записи о своих расходах. Приложение также поддерживает экспорт данных в форматах PDF и Excel.

## Требования

Перед запуском проекта убедитесь, что у вас установлены следующие инструменты:

- Python 3.x
- PostgreSQL

## Установка и настройка

### Установите PostgreSQL

Если PostgreSQL не установлен, скачайте и установите его с официального сайта: https://www.postgresql.org/download/

### Клонируйте репозиторий

Склонируйте проект на вашу локальную машину:

```bash
git clone https://github.com/bexiiiii/Expense-Tracker-.git
cd Expense-Tracker
```

### Создайте виртуальное окружение

Создайте виртуальное окружение:

```bash
python -m venv venv
```

### Активируйте виртуальное окружение

На Windows:

```bash
venv\Scripts\activate
```

На macOS и Linux:

```bash
source venv/bin/activate
```

### Установите зависимости

Установите все необходимые зависимости из файла `requirements.txt`:

```bash
pip install -r requirements.txt
```

### Настройте базу данных PostgreSQL

Создайте базу данных и пользователя в PostgreSQL, используя команду:

```bash
psql -U postgres
```

Создайте базу данных:

```bash
CREATE DATABASE expense_tracker;
CREATE USER your_user WITH PASSWORD 'your_password';
GRANT ALL PRIVILEGES ON DATABASE expense_tracker TO your_user;
```

### Настройте переменные окружения

Создайте файл `.env` в корневой директории проекта и добавьте в него следующие строки:

```ini
SECRET_KEY=your_secret_key
DEBUG=True
DB_NAME=expense_tracker
DB_USER=your_user
DB_PASSWORD=your_password
DB_HOST=localhost
DB_PORT=5432
```

### Примените миграции

Примените миграции для настройки базы данных:

```bash
python manage.py migrate
```

### Создайте суперпользователя

Создайте суперпользователя для админ-панели:

```bash
python manage.py createsuperuser
```

### Запустите сервер

Запустите сервер:

```bash
python manage.py runserver
```

Теперь вы можете открыть проект в браузере по адресу [http://127.0.0.1:8000/](http://127.0.0.1:8000/).

## Лицензия

Этот проект лицензирован под MIT License.
