from abstract_repository import AbstractRepository
from classes.reserva import Reserva

class ReservasRepository(AbstractRepository):

  def inserir_reserva(self, reserva: Reserva):
    sql = """INSERT INTO reservas (quantidade_pessoas, data_inicio, data_fim, valor, usuario)
        VALUES (:quantidade_pessoas, :data_inicio, :data_fim, :valor, :usuario)"""
    
    params = reserva.__dict__

    self.execute(sql, params)