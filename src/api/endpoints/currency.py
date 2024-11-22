from typing import Annotated
from fastapi import APIRouter, Depends, HTTPException, status

from core.security import get_current_user
from api.models.token import TokenData
from api.models.currency import Currency, CurrencyResponse
from utils.external_api import (
    fetch_exchange_rates,
    validate_currency_code,
    currency_list
)


router_currency = APIRouter(prefix="/currency", tags=["currency"])


@router_currency.get("/exchange")
async def get_exchange_rates(
    base_currency: str,
    user: Annotated[TokenData, Depends(get_current_user)]
):
    '''
    Защищённая конечная точка для получения обменных курсов.
    '''
    exchange_data = await fetch_exchange_rates(base_currency)
    return {
        "base_currency": base_currency,
        "rates": exchange_data.get("conversion_rates", {}),
        "last_update": exchange_data.get("time_last_update_utc", "unknown")
    }


@router_currency.get("/convert", response_model=CurrencyResponse)
async def convert_currency(
    currency: Currency,
    user: Annotated[TokenData, Depends(get_current_user)]
):
    '''
    Защищённая конечная точка для конвертации валют.
    '''
    exchange_data = await fetch_exchange_rates(currency.from_currency)

    await validate_currency_code(currency.from_currency)
    await validate_currency_code(currency.to_currency)

    rate = exchange_data["conversion_rates"].get(currency.to_currency)
    if not rate:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail=f"Exchange rate for {currency.to_currency} not found."
        )
    converted_amount = currency.amount * rate
    converted_currency = CurrencyResponse(
        **currency.model_dump(),
        rate=rate,
        converted_amount=converted_amount
        )
    return converted_currency


@router_currency.get("/list")
async def get_currency_list(
    user: Annotated[TokenData, Depends(get_current_user)],
    base_currency: str = "USD"
):
    '''
    Защищенная конечная точка для отображения
    списка поддерживаемых валют и их кодов.
    '''
    return await currency_list(base_currency)
