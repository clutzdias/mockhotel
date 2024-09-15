from abstract_repository import AbstractRepository
from classes.reserva import Reserva
from classes.cancelamento_reserva import CancelamentoReserva

class ReservasRepository(AbstractRepository):

  def inserir_reserva(self, reserva: Reserva):
    sql = """INSERT INTO reservas (quantidade_pessoas, data_inicio, data_fim, valor, usuario)
        VALUES (:quantidade_pessoas, :data_inicio, :data_fim, :valor, :usuario)
        RETURNING reserva;"""
    
    params = reserva.__dict__

    dados = self.fetchOne(sql, params)

    id_reserva = dados['id']

    sql = """INSERT INTO reservas_quartos (reserva, quarto)
          VALUES (:reserva, :quarto);"""
    
    params2 = [{'reserva': id_reserva, 'quarto': quarto.id} for quarto in reserva.quartos]

    self.executeMany(sql, params2)
  
  def cancelar_reserva(self, cancelamento_reserva: CancelamentoReserva):

    sql = """INSERT INTO cancelamentos_reservas (reserva, motivo, data_cancelamento, gerou_nova_reserva)
            VALUES (:reserva, :motivo, :data_cancelamento, :gerou_nova_reserva);"""
    
    params = {
      "reserva": cancelamento_reserva.reserva.reserva,
      "motivo": cancelamento_reserva.motivo,
      "data_cancelamento": cancelamento_reserva.data_cancelamento,
      "gerou_nova_reserva": cancelamento_reserva.gerou_nova_reserva
    }

    self.execute(sql, params)

    sql = """DELETE FROM reservas_quartos WHERE reserva = :reserva;"""

    params = {"reserva": cancelamento_reserva.reserva.reserva}

    self.execute(sql, params)

  def consulta_reservas_por_usuario(self, id_usuario):

    sql = """SELECT 
              r.quantidade_pessoas,
              r.data_inicio,
              r.data_fim,
              r.valor,
              q.quantidade_acomodacoes,
              q.tipo_acomodacoes,
              q.tipo_quarto
            FROM reservas r
            JOIN reservas_quartos rq ON r.reserva = rq.reserva
            JOIN quartos q ON q.quarto = rq.quarto
            WHERE r.usuario = :usuario;"""
    
    params = {"usuario": id_usuario}

    return self.fetchAll(sql, params)
  
  def alterar_reserva(self, reserva: Reserva, alteracao_quartos: bool):

    if reserva.reserva is None:
      pass

    sql = """UPDATE reservas
            SET quantidade_pessoas = :quantidade_pessoas, 
            data_inicio = :data_inicio, 
            data_fim = :data_fim, 
            valor = :valor
            WHERE reserva = :reserva;"""
    
    params = {
      "quantidade_pessoas": reserva.quantidade_pessoas,
      "data_inicio": reserva.data_inicio,
      "data_fim": reserva.data_fim,
      "valor": reserva.valor,
      "reserva": reserva.reserva
    }

    self.execute(sql, params)

    if alteracao_quartos:
      sql = "DELETE FROM reservas_quartos WHERE reserva = :reserva;"

      params = {"reserva": reserva.reserva}

      self.execute(sql, params)

      sql = """INSERT INTO reservas_quartos (reserva, quarto)
          VALUES (:reserva, :quarto);"""
    
      params2 = [{'reserva': reserva.reserva, 'quarto': quarto.id} for quarto in reserva.quartos]

      self.executeMany(sql, params2)


       