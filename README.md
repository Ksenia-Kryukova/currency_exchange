### Пример файла `README.md`

```markdown
# Currency Exchange API

## Описание проекта

Currency Exchange API — это сервис, который позволяет пользователям получать доступ к данным об обменных курсах валют в режиме реального времени и выполнять конвертацию валют. Проект разработан с использованием **FastAPI** и обеспечивает защиту данных с помощью **JWT-аутентификации**. Данные об обменных курсах запрашиваются из внешнего API, а информация о пользователях хранится в **MongoDB**.

---

## Возможности

- Получение списка поддерживаемых валют и их кодов.
- Конвертация валют на основе актуальных курсов.
- Защищённый доступ к данным с использованием JWT-аутентификации.
- Работа с MongoDB для хранения пользовательских данных и истории операций.
- Интеграция с внешним API для получения свежих обменных курсов.

---

## Технологии

- **Backend**: FastAPI
- **Authentication**: JWT
- **Database**: MongoDB
- **External API**: Используется для получения данных об обменных курсах
- **Environment Variables**: Python-dotenv

---

## Установка и запуск

### 1. Клонирование репозитория

```bash
git clone https://github.com/username/currency-exchange-api.git
cd currency-exchange-api
```

### 2. Установка зависимостей

Создайте и активируйте виртуальное окружение, затем установите зависимости:

```bash
python -m venv venv
source venv/bin/activate  # Для Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 3. Настройка переменных окружения

Создайте файл `.env` и укажите переменные:
```
MONGODB_URI=mongodb://localhost:27017
EXCHANGE_API_URL=https://api.example.com/latest
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
    "currencies": {
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
currency-exchange-api/
│
├── app/
│   ├── main.py                # Точка входа в приложение
│   ├── models/                # Pydantic модели
│   ├── routes/                # Маршруты приложения
│   ├── services/              # Взаимодействие с внешними API
│   └── utils/                 # Утилиты (валидация, хэши, JWT)
│
├── tests/                     # Тесты приложения
├── requirements.txt           # Зависимости
├── .env                       # Переменные окружения
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

Автор: Ксения 
Email: ksyusha-kryukova@bk.ru 
GitHub: 

---
```# currency_exchange
