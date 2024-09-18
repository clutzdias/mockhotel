import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from services.reservas_service import ReservaService
from repositories.reservas_repository import ReservasRepository
from classes.reserva import Reserva
from classes.cancelamento_reserva import CancelamentoReserva

dados = {
  "quantidade_pessoas": 2,
  "data_inicio": '2024-10-01',
  "data_fim": '2024-10-05',
  "valor": 255.00,
  "usuario": 'ed06c339-0120-4841-bf50-91ec656fffaa',
  "quartos": [
    {
      "quarto": '9b4e129a-d6f2-4123-ac7b-786b7d4f16d6',
      "hotel": 'fa063e11-d6b9-49c7-b56a-be5d759edf7d',
      "quantidade_acomodacoes": 2,
      "tipo_acomodacoes": 'CAMA_CASAL',
      "tipo_quarto": 'STANDARD_NAO_FUMANTES'
    }
  ]
}

class TestReservasSuccess:
    
  def test_criar_reserva(self):

    service = ReservaService(ReservasRepository())

    assert isinstance(service.fazer_reserva(dados), Reserva)

  def test_alterar_reserva(self):

    service = ReservaService(ReservasRepository())

    dados['reserva'] = ''
    dados['data_inicio'] = '2024-10-10'
    dados['data_fim'] = '2024-10-15'
    
    assert isinstance(service.alterar_reserva(dados), Reserva)

  def test_cancelar_reserva(self):

    service = ReservaService(ReservasRepository())

    dados_cancelamento = {"reserva": '',
                          "motivo": 'Teste cancelamento de reserva',
                          "data_cancelamento": '2024-09-18'
                          }

    assert isinstance(service.cancelar_reserva(dados_cancelamento), CancelamentoReserva)


    