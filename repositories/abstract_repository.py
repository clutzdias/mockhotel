import psycopg2
from psycopg2 import sql
from typing import List

db_connection_params = {
  'dbname': 'mockhotel',
  'user': 'postgres',
  'password': 'postgres',
  'host': 'localhost',
  'port': 5432
}

class AbstractRepository:
    
  def __init__(self):
    self.connection = None
    self.cursor = None
    self.db_connection_params = db_connection_params
  
  def set_connection(self):
    try:
      if self.connection:
        self.connection.close()
        
      self.connection = psycopg2.connect(**self.db_connection_params)
      self.cursor = self.connection.cursor()
    except Exception as e:
      raise RuntimeError(f'Falha ao conectar-se ao banco de dados: {e}')
    
  def begin(self):
    try:
      if self.connection is None:
        raise RuntimeError('Conexão não inicializada.')
      self.connection.autocommit = False
    except Exception as e:
      raise RuntimeError(f'Falha ao iniciar transação: {e}')
    
  def commit(self):
    try:
      if self.connection is None:
        raise RuntimeError('Conexão não inicializada.')
      self.connection.commit()
      self.connection.autocommit = True
    except Exception as e:
      raise RuntimeError(f'Falha ao commitar transação: {e}') 

  def rollback(self):
    try:
      if self.connection is None:
        raise RuntimeError('Conexão não inicializada.')
      self.connection.rollback()
      self.connection.autocommit = True
    except Exception as e:
      raise RuntimeError(f'Falha ao dar rollback na transação: {e}') 

  def __execute(self, sql: str, params: dict):
    from sqlparams import SQLParams
    if not isinstance(params, dict):
      params = params.__dict__

    try:
      sql2, params2 = SQLParams('named', 'format').format(sql, params)
      cursor = self.connection.cursor()
      cursor.execute(sql2,params2)
    except Exception as e:
      ##Colocar log de exceção
      pass

    return cursor

  def execute(self, sql: str, params: dict):
    try:
      cursor = None
      cursor = self.__execute(sql, params)
    finally:
      if cursor != None:
        cursor.close()

  def fetchAll(self, sql: str, params: dict) -> List[dict]:
    try:
      cursor = None
      try:
        cursor = self.__execute(sql, params)
        return cursor.fetchall()
      except Exception as e:
        raise
    finally:
      if cursor != None:
        cursor.close()

  def fetchOne(self, sql: str, params: dict) -> dict:
    try:
      cursor = None
      try:
        cursor = self.__execute(sql, params)
        if cursor is not None:
          dados = cursor.fetchall()
          if len(dados) > 0:
            return dados[0]  
      except Exception as e:
        raise
    finally:
      if cursor != None:
        cursor.close()

if __name__ == '__main__':
  repository = AbstractRepository()

  sql = "select * from usuarios where nome = :fulano"

  params = {"fulano": 'Fulano da Silva'}

  repository.set_connection()

  dados = repository.fetchAll(sql, params)

  print(dados)

    
      

    