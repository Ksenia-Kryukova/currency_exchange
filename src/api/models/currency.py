from pydantic import BaseModel


class Base(BaseModel):
    pass


class Currency(Base):
    amount: int = 1
    from_currency: str
    to_currency: str


class CurrencyResponse(Currency):
    rate: float
    converted_amount: float
