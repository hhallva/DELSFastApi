from pydantic import BaseModel


class StreetStat(BaseModel):
    streetName: str
    cars: int
    trucks: int
    buses: int
    averageSpeed: int
    amount: int = 0

    @staticmethod
    def calculate_amount(values):
        values.amount = values.cars + values.trucks + values.buses
        return values
