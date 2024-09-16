from abstract_repository import AbstractRepository

class QuartosRepository(AbstractRepository):
    
  def consulta_quartos_disponiveis_por_hotel_e_periodo(self, hotel, data_inicio, data_fim):

    sql = """SELECT 
              q.quantidade_acomodacoes,
              q.tipo_acomodacoes,
              q.tipo_quarto
            FROM quartos q
            JOIN hoteis h on q.hotel = h.hotel
            WHERE h.hotel = :hotel 
            AND quarto IN (
              SELECT rq.quarto
              FROM reservas_quartos rq
              JOIN reservas r ON r.reserva = rq.reserva
              WHERE r.hotel = :hotel
              AND r.data_fim < :data_inicio
              AND r.data_inicio > :data_fim)"""
    
    params = {"hotel": hotel, "data_inicio": data_inicio, "data_fim": data_fim}

    return self.fetchAll(sql, params)