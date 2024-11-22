# Currency Exchange API

## Описание проекта

Currency Exchange API — это сервис, который позволяет пользователям получать доступ к данным об обменных курсах валют в режиме реального времени и выполнять конвертацию валют. Проект разработан с использованием **FastAPI**, используя принципы **REST API** и обеспечивает защиту данных с помощью **JWT-аутентификации**. Данные об обменных курсах запрашиваются из внешнего API, а информация о пользователях хранится в **MongoDB**.

---

## Возможности

- Получение списка поддерживаемых валют и их кодов.
- Конвертация валют на основе актуальных курсов.
- Защищённый доступ к данным с использованием JWT-аутентификации.
- Работа с MongoDB для хранения пользовательских данных.
- Интеграция с внешним API для получения свежих обменных курсов.

---

## Технологии

- **Backend**: FastAPI
- **API Type**: REST API
- **Authentication**: JWT
- **Database**: MongoDB
- **External API**: Используется для получения данных об обменных курсах
- **Environment Variables**: Pydantic settings

---

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/username/currency_exchange.git
cd currency_exchange
```

### 2. Установка зависимостей

Создайте и активируйте виртуальное окружение, затем установите зависимости:

```bash
python3 -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Настройка переменных окружения

Создайте файл `.env` и укажите переменные:
```
DB_HOST=localhost
DB_PORT=27017
DB_NAME=your_db_name
EXCHANGE_API_URL=https://v6.exchangerate-api.com/v6/{your_api_key}/latest/
EXCHANGE_API_KEY=your_api_key
SECRET_KEY=your_secret_key
ACCESS_TOKEN_EXPIRE_MINUTES=30
```

### 4. Запуск MongoDB

Запустите MongoDB локально или используйте облачный сервис.

### 5. Запуск приложения

```bash
uvicorn app.main:app --reload
```

Приложение будет доступно по адресу: `http://127.0.0.1:8000`

---

## Примеры использования

### Получение списка поддерживаемых валют
**Endpoint**: `/currency/list/`  
**Метод**: `GET`  
**Пример ответа**:
```json
{
    "conversion_rates": {
        "USD": "United States Dollar",
        "EUR": "Euro",
        "GBP": "British Pound Sterling",
        ...
    }
}
```

### Конвертация валют
**Endpoint**: `/currency/convert/`  
**Метод**: `GET`  
**Требуется JWT-токен**  
**Пример запроса**:
```json
{
    "amount": 100,
    "from_currency": "USD",
    "to_currency": "EUR"
}
```
**Пример ответа**:
```json
{
    "amount": 100,
    "from_currency": "USD",
    "to_currency": "EUR",
    "rate": 0.85,
    "converted_amount": 85
}
```

---

## Структура проекта

```
currency_exchange/
│
├── src/
│   ├── api/                   
│   │    ├── endpoints/        # Маршруты приложения
│   │    ├── models/           # Pydantic модели
│   ├── core/                  # Утилиты (валидация, хэши, JWT)
│   ├── db/                    # Взаимодействие с БД
│   └── utils/                 # Взаимодействие с внешними API
│
├── tests/                     # Тесты приложения
├── requirements.txt           # Зависимости
├── .env                       # Переменные окружения
├── main.py                    # Точка входа в приложение
├── pyproject.toml             # 
└── README.md                  # Документация
```

---

## Тестирование

Для запуска тестов используйте:
```bash
pytest
```

---

## Разработка и идеи для улучшения

- Добавить поддержку истории операций пользователя.
- Расширить список внешних API для данных об обменных курсах.
- Добавить кэширование курсов для оптимизации запросов.

---

## Контакты

Автор: Ксения Маслова
Email: ksyusha-kryukova@bk.ru 
GitHub: github.com/Ksenia-Kryukova

---
```# currency_exchange
