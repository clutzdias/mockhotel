from pydantic import BaseModel
from uuid import UUID
from typing import Optional
from datetime import datetime

from classes.reserva import Reserva

class CancelamentoReserva(BaseModel):
  cancelamentoreserva: Optional[UUID]
  reserva: UUID
  motivo: str
  data_cancelamento: datetime = datetime.now()
  gerou_nova_reserva: Optional[bool]
  nova_reserva: Optional[Reserva]