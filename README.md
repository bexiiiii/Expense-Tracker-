# Expense Tracker

## 1. Описание проекта

Expense Tracker — это веб-приложение на Django для управления личными финансами. Оно позволяет пользователям отслеживать свои расходы, распределять их по категориям, экспортировать отчеты в различные форматы и управлять бюджетом.

## 2. Основные функции

- **Регистрация и аутентификация пользователей**
- **Добавление, редактирование и удаление расходов**
- **Категоризация расходов**
- **Экспорт данных в PDF и Excel**
- **Аналитика расходов** (графики, отчеты)
- **Поиск и фильтрация записей**

## 3. Технологии

- **Backend**: Django
- **Frontend**: HTML, CSS
- **База данных**: PostgreSQL
- **Дополнительные библиотеки**:
  - **ReportLab** — для генерации PDF-отчетов
  - **OpenPyXL** — для работы с Excel
  - **django-allauth** — для аутентификации



## 4. Установка и настройка

### 4.1. Клонирование репозитория

```bash
git clone https://github.com/bexiiiii/Expense-Tracker-.git
cd Expense-Tracker-
```

### 4.2. Создание виртуального окружения и установка зависимостей

```bash
python -m venv venv
source venv/bin/activate  # macOS/Linux
venv\Scripts\activate    # Windows
pip install -r requirements.txt
```

### 4.3. Настройка базы данных

Открываем `settings.py` и указываем параметры PostgreSQL:

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'expense_db',
        'USER': 'username',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}
```

### 4.4. Применение миграций и запуск сервера

```bash
python manage.py migrate
python manage.py createsuperuser  # Создание администратора
python manage.py runserver
```

Приложение доступно по адресу: `http://127.0.0.1:8000`

## 5. Структура проекта

```bash
Expense-Tracker/
├── expense_tracker/        # Основное приложение Django
│   ├── migrations/         # Миграции базы данных
│   ├── templates/          # HTML-шаблоны
│   ├── static/             # CSS, JS, изображения
│   ├── views.py            # Логика представлений
│   ├── models.py           # Модели базы данных
│   ├── urls.py             # Маршрутизация
│   ├── forms.py            # Django Forms
├── api/                    # API (если реализован)
│   ├── serializers.py      # Сериализация данных
│   ├── views.py            # API-вьюхи
│   ├── urls.py             # API-маршруты
├── requirements.txt        # Список зависимостей
├── manage.py               # Django-скрипт
└── README.md               # Этот файл
```

## 6. API (если есть)

Если в проекте есть API, добавьте примеры запросов:

```bash
GET /api/expenses/            # Получить список расходов
POST /api/expenses/           # Добавить новый расход
PUT /api/expenses/{id}/       # Редактировать расход
DELETE /api/expenses/{id}/    # Удалить расход
```

## 7. Экспорт данных

Приложение позволяет экспортировать данные в PDF и Excel:

- **PDF**: `/export/pdf/`
- **Excel**: `/export/excel/`

## 8. Развертывание

Для развертывания на сервере (например, Heroku, DigitalOcean):

1. Настроить переменные окружения (`.env` файл)
2. Использовать Gunicorn и Nginx для продакшн-версии
3. Настроить статические файлы (`collectstatic`)

## 9. Алгоритм работы



## 10. Контакты

Разработчик: **bexiiiii**\
GitHub: [https://github.com/bexiiiii](https://github.com/bexiiiii)

