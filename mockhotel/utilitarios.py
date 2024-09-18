import datetime


def formataDataEntrada(data:str):
    if data is None:
        return datetime.datetime.now()
    return datetime.datetime.strptime(data, "%Y-%m-%d")

def formataDataSaida(data: datetime.datetime):
    return data.strftime('%Y-%m-%d')
