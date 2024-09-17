from exceptions import QuartosIndisponiveisPorPeriodo, ReservaInvalida, QuartosInsuficientesParaReserva, CancelamentoReservaInvalido, ExcecaoManual, AlteracaoReservaInvalida
from repositories import AbstractRepository

class AbstractView:
  def __init__(self):
    AbstractRepository.set_connection()

  def post():
    pass

  def get():
    pass

  def patch():
    pass

  def cancelar():
    pass

  def tratar_resposta(self, dados, excecao = None):
    if excecao is None:
      return {"http_status": 200,
              "dados": dados}

    if (isinstance(excecao, ReservaInvalida)
        or isinstance(excecao, CancelamentoReservaInvalido)
        or isinstance(excecao, AlteracaoReservaInvalida)
        or isinstance(excecao, ExcecaoManual)):
      return {"http_status": 400,
            "mensagem": excecao.mensagem,
            "erro": excecao,
            "dados": dados}
    elif (isinstance(excecao, QuartosInsuficientesParaReserva)
        or isinstance(excecao, QuartosIndisponiveisPorPeriodo)):
      return {"http_status": 422,
            "mensagem": excecao.mensagem,
            "erro": excecao,
            "dados": dados}
    else:
      return {"http_status": 500,
            "erro": excecao,
            "dados": dados}

    