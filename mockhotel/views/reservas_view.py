from flask import request, jsonify, make_response
from mockhotel.services.reservas_service import ReservaService
from mockhotel.repositories.reservas_repository import ReservasRepository
from mockhotel.views.abstract_view import AbstractView
from ..exceptions import ExcecaoManual

class ReservasView(AbstractView):

  def __init__(self):
    super().__init__()
    self.service = ReservaService(ReservasRepository())

  def post(self):
    try:
      body = request.get_json()

      reserva = self.service.fazer_reserva(body)

      retorno = jsonify(reserva.__dict__)
      retorno = self.tratar_resposta(retorno)
      return make_response(retorno, retorno["http_status"])
    except Exception as e:
      retorno = self.tratar_resposta([], e)
      return make_response(retorno, retorno["http_status"])
 
  def get(self):
    try:
      id_usuario = request.args.get('usuario')
      if id_usuario is None:
        raise ExcecaoManual("O usuário não foi informado")
      
      reservas = self.service.get_reservas_usuario(id_usuario)

      retorno = jsonify(reservas)
      return self.tratar_resposta(retorno)
    except Exception as e:
      return self.tratar_resposta([], e)
  
  def patch(self, id_reserva):
    try:
      body = request.get_json()

      if id_reserva is not None:
        body["reserva"] = id_reserva

      reserva = self.service.alterar_reserva(body)

      retorno = jsonify(reserva.__dict__)
      return self.tratar_resposta(retorno)
    except Exception as e:
      return self.tratar_resposta([], e)

  def cancelar(self, id_reserva):
    try:
      body = request.get_json()

      if id_reserva is not None:
        body["reserva"] = id_reserva

      reserva = self.service.cancelar_reserva(body)

      retorno = jsonify(reserva.__dict__)
      retorno = self.tratar_resposta(retorno)
    except Exception as e:
      retorno = self.tratar_resposta([], e)