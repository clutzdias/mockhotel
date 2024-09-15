from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

from reserva import Reserva

class CancelamentoReserva(BaseModel):
  cancelamentoreserva: Optional[UUID]
  reserva: Reserva
  motivo: str
  data_cancelamento: datetime
  gerou_nova_reserva: bool