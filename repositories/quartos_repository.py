from abstract_repository import AbstractRepository

class QuartosRepository(AbstractRepository):
    
  def consulta_quartos_disponiveis_por_hotel_e_data(self, hotel, data):

    sql = """SELECT 
              q.quantidade_acomodacoes,
              q.tipo_acomodacoes,
              q.tipo_quarto
            FROM quartos q
            JOIN hoteis h on q.hotel = h.hotel
            WHERE h.hotel = :hotel 
            AND quarto NOT IN (
              SELECT rq.quarto
              FROM reservas_quartos rq
              JOIN reservas r ON r.reserva = rq.reserva
              WHERE r.hotel = :hotel
              AND :data BETWEEN r.data_inicio AND r.data_fim)"""
    
    params = {"hotel": hotel, "data": data}

    return self.fetchAll(sql, params)