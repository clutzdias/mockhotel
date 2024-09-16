
class ExcecaoManual(Exception):
  def __init__(self, mensagem, detalhes = None):
    self.mensagem = mensagem
    self.detalhes = detalhes
  
  def __dict__(self):
    if self.detalhes is not None:
      return {
        "erro": self.mensagem,
        "detalhes": self.detalhes
      }
    return {"erro": self.mensagem}

class ReservaInvalida(ExcecaoManual):
  pass

class QuartosInsuficientesParaReserva(ExcecaoManual):
  pass

class QuartosIndisponiveisPorPeriodoException(ExcecaoManual):
  pass

class AlteracaoReservaInvalida(ExcecaoManual):
  pass

class CancelamentoReservaInvalido(ExcecaoManual):
  pass

class QuantidadePessoasInvalida(ExcecaoManual):
  pass

class ReservaJaEfetuadaException(ExcecaoManual):
  pass
