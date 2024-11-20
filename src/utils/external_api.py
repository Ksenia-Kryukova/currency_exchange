import requests
from fastapi import HTTPException, status


API_URL = "https://api.exchangerate-api.com/v4/latest/"
TIMEOUT = 10


def fetch_exchange_rates(base_currency: str) -> dict:
    '''
    Получает текущие курсы обмена для указанной базовой валюты.
    '''
    try:
        response = requests.get(f"{API_URL}{base_currency}", timeout=TIMEOUT)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error fetching exchange rates: {str(e)}"
        )


def validate_currency_code(
        currency_code: str,
        available_codes: list[str]
) -> None:
    '''
    Проверяет, существует ли указанный код валюты.
    '''
    if currency_code not in available_codes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Invalid currency code: {currency_code}. Available codes: {', '.join(available_codes)}"
        )


def currency_list(base_currency: str):
    '''
    Отображает список поддерживаемых валют и их кодов.
    '''
    exchange_data = fetch_exchange_rates(base_currency)
    available_codes = exchange_data.get("rates", {}).keys()
    return available_codes
