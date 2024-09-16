from repositories.reservas_repository import ReservasRepository
from exceptions import QuartosIndisponiveisPorPeriodo
from classes.quarto import Quarto
from classes.reserva import Reserva

class ReservaService:
    
  def __init__(self, reserva_repository: ReservasRepository):
    self.repository = reserva_repository
  
  def fazer_reserva(self, dados):
    pass
  
  def cancelar_reserva(self, dados):
    pass

  def alterar_reserva(self, dados):
    pass

  def consulta_quartos_disponiveis(self, hotel, data_inicio, data_fim):
    from repositories.quartos_repository import QuartosRepository

    repository = QuartosRepository()

    dados = repository.consulta_quartos_disponiveis_por_hotel_e_periodo(hotel, data_inicio, data_fim)

    retorno = []
    if len(dados) == 0:
      raise QuartosIndisponiveisPorPeriodo("Não foram encontrados quartos disponíveis para o período.", 
                                           f'Data de Início: {data_inicio}, Data final: {data_fim}')

    else:
      for dado in dados:
        quarto = Quarto(quarto=dado["quarto"],
                        hotel=dado["hotel"],
                        quantidade_acomodacoes=dado["quantidade_acomodacoes"],
                        tipo_acomodacoes=dado["tipo_acomodacoes"],
                        tipo_quarto=dado["tipo_quarto"])
        retorno.append(quarto)

    return retorno
    
