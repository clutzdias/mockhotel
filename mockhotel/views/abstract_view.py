
from mockhotel.repositories.abstract_repository import AbstractRepository

class AbstractView:
  def __init__(self):
    self.repository = AbstractRepository()
    self.repository.set_connection()

  def post():
    pass

  def get():
    pass

  def patch():
    pass

  def cancelar():
    pass

  def tratar_resposta(self, dados, excecao = None):
    import mockhotel.exceptions as Exceptions
    if excecao is None:
      return {"http_status": 200,
              "dados": dados}

    if (isinstance(excecao, Exceptions.ReservaInvalida)
        or isinstance(excecao, Exceptions.CancelamentoReservaInvalido)
        or isinstance(excecao, Exceptions.AlteracaoReservaInvalida)
        or isinstance(excecao, Exceptions.ExcecaoManual)):
      return {"http_status": 400,
            "mensagem": excecao.mensagem,
            "dados": dados}
    elif (isinstance(excecao, Exceptions.QuartosInsuficientesParaReserva)
        or isinstance(excecao, Exceptions.QuartosIndisponiveisPorPeriodo)):
      return {"http_status": 422,
            "mensagem": excecao.mensagem,
            "dados": dados}
    else:
      return {"http_status": 500,
            "erro": 'Falha ao executar a operação.',
            "dados": dados}

    