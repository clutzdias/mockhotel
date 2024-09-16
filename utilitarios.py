import datetime

def formataDataEntrada(data:str):
    data = datetime.datetime.strptime(data, "%Y-%m-%d")
    return data.strftime('%Y-%m-%d')

def formataDataSaida(data: datetime.datetime):
    return data.strftime('%Y-%m-%d')