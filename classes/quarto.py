from pydantic import BaseModel
from uuid import UUID
from typing import Optional

from enums.tipo_acomodacoes import TipoAcomodacoes
from enums.tipo_quarto import TipoQuarto

class Quarto(BaseModel):
  quarto: Optional[UUID]
  hotel: UUID
  quantidade_acomodacoes: int
  tipo_acomodacoes: TipoAcomodacoes
  tipo_quarto: TipoQuarto