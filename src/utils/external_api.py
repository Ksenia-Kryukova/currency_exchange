import httpx
from fastapi import HTTPException, status
from core.config import settings


TIMEOUT = 10


async def fetch_exchange_rates(base_currency: str) -> dict:
    '''
    Получает текущие курсы обмена для указанной базовой валюты.
    '''
    try:
        async with httpx.AsyncClient(timeout=TIMEOUT) as client:
            response = await client.get(
                f"{settings.ASYNC_API_URL}{base_currency}"
                )
            response.raise_for_status()
            return response.json()
    except httpx.RequestError as e:
        raise HTTPException(
            status_code=status.HTTP_503_SERVICE_UNAVAILABLE,
            detail=f"Error fetching exchange rates: {str(e)}"
        )
    except httpx.HTTPStatusError as e:
        raise HTTPException(
            status_code=e.response.status_code,
            detail=f"Error response {e.response.status_code}:{e.response.text}"
        )


async def currency_list(base_currency: str):
    '''
    Отображает список поддерживаемых валют и их кодов.
    '''
    exchange_data = await fetch_exchange_rates(base_currency)
    available_codes = exchange_data.get("conversion_rates", {}).keys()
    return available_codes


async def validate_currency_code(currency_code: str) -> None:
    '''
    Проверяет, существует ли указанный код валюты.
    '''
    available_codes = await currency_list(currency_code)
    if currency_code not in available_codes:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=(
                f"Invalid currency code: {currency_code}. "
                f"Available codes: {', '.join(available_codes)}"
            )
        )
