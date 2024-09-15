from pydantic import BaseModel
from uuid import UUID
from datetime import date
from decimal import Decimal
from typing import Optional, List

from quarto import Quarto

class Reserva(BaseModel):
  reserva: Optional[UUID]
  quantidade_pessoas: int
  data_inicio: date
  data_fim: date
  valor: Decimal
  usuario: UUID
  quartos: List[Quarto]
    