from flask import Blueprint, request

from mockhotel.views.reservas_view import ReservasView

blue_print = Blueprint('main', __name__)

@blue_print.route('/reservas', methods=['GET', 'POST'])
def reservas():
  if request.method == 'POST':
    return ReservasView().post()
  else:
    return ReservasView().get()

@blue_print.route('/reservas/<id_reserva>', methods=['PATCH', 'DELETE'])
def reservas_id(id_reserva):
  if request.method == 'PATCH':
    return ReservasView().patch(id_reserva)
  else:
    return ReservasView().cancelar(id_reserva)
  
def register_routes(app):
  app.register_blueprint(blue_print)



