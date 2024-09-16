import utilitarios

from repositories.reservas_repository import ReservasRepository
from exceptions import QuartosIndisponiveisPorPeriodo, ReservaInvalida, QuartosInsuficientesParaReserva, CancelamentoReservaInvalido, ExcecaoManual, AlteracaoReservaInvalida
from classes.quarto import Quarto
from classes.reserva import Reserva
from classes.cancelamento_reserva import CancelamentoReserva

class ReservaService:
    
  def __init__(self, reserva_repository: ReservasRepository):
    self.repository = reserva_repository
  
  def fazer_reserva(self, dados):
    if dados is None or len(dados) == 0:
      raise ReservaInvalida("Não foram informados dados para a reserva.")
    
    if "quartos" not in dados or len(dados["quartos"]) == 0:
      raise ReservaInvalida("Não foram selecionados quartos para a reserva.")
    
    quartos = []
    quantidade_leitos = 0

    for dado in dados["quartos"]:
      quarto = Quarto(quarto=dado["quarto"],
                      hotel=dado["hotel"],
                      quantidade_acomodacoes=dado["quantidade_acomodacoes"],
                      tipo_acomodacoes=dado["tipo_acomodacoes"],
                      tipo_quarto=dado["tipo_quarto"])
      
      quantidade_leitos += quarto.quantidade_acomodacoes
      
      quartos.append(quarto)

    if quantidade_leitos < dados['quantidade_pessoas']:
      raise QuartosInsuficientesParaReserva('A quantidade de leitos disponíveis nos quartos informados' + 
                                            'é inferior à quantidade de pessoas da reserva.')

    try:
      reserva = Reserva(quantidade_pessoas=dados["quantidade_pessoas"],
                        data_inicio=utilitarios.formataDataEntrada(dados["data_inicio"]),
                        data_fim=utilitarios.formataDataEntrada(dados["data_fim"]),
                        valor=dados["valor"],
                        usuario=dados["usuario"],
                        quartos=quartos
                        )
      
      self.repository.inserir_reserva(reserva)

    except Exception as e:
      raise ExcecaoManual("Falha ao efetuar a reserva", e)

    return reserva

  def cancelar_reserva(self, dados):
    if dados is None or len(dados) == 0:
      raise CancelamentoReservaInvalido("Não foram informados dados para o cancelamento")
    elif "reserva" not in dados or dados["reserva"] is None:
      raise CancelamentoReservaInvalido("Não foi informada uma reserva para o cancelamento")
    
    try:
      cancelamento_reserva = CancelamentoReserva(reserva=dados["reserva"],
                                                 motivo=dados["motivo"],
                                                 gerou_nova_reserva=dados["nova_reserva"] is not None if "nova_reserva" in dados else False,
                                                 nova_reserva=dados["nova_reserva"])
      self.repository.cancelar_reserva(cancelamento_reserva)
    except Exception as e:
      raise ExcecaoManual('Falha ao efetuar o cancelamento da reserva.', e)

  def alterar_reserva(self, dados):
    if dados is None or len(dados) == 0:
      raise AlteracaoReservaInvalida("Não foram informados dados para fazer a alteracao da reserva.")
    elif "reserva" not in dados or dados["reserva"] is None:
      raise AlteracaoReservaInvalida("Não foi informada uma reserva para alteração")
    
    id_reserva = self.repository.verifica_reserva_valida(dados["reserva"])

    if id_reserva is None:
      raise AlteracaoReservaInvalida("Não foi encontrada uma reserva registrada para o parâmetro informado", dados["reserva"])
    
    lista_quartos_alterados = []
    alteracao_quartos = False

    if "quartos" in dados and dados["quartos"] is not None:
      alteracao_quartos = True
      for dado in dados["quartos"]:

        quarto = Quarto(quarto=dado["quarto"],
                        hotel=dado["hotel"],
                        quantidade_acomodacoes=dado["quantidade_acomodacoes"],
                        tipo_acomodacoes=dado["tipo_acomodacoes"],
                        tipo_quarto=dado["tipo_quarto"])
        lista_quartos_alterados.append(quarto)
    
    try:
      reserva = Reserva(reserva=id_reserva,
                        quantidade_pessoas=dados["quantidade_pessoas"],
                        data_inicio=utilitarios.formataDataEntrada(dados["data_inicio"]),
                        data_fim=utilitarios.formataDataEntrada(dados["data_fim"]),
                        valor=dados["valor"],
                        usuario=dados["usuario"],
                        quartos=lista_quartos_alterados
                        )
      
      self.repository.alterar_reserva(reserva, alteracao_quartos)
    except Exception as e:
      raise ExcecaoManual("Falha ao efetuar a alteração da reserva", e)

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
    
