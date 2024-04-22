from datetime import datetime
import pytz

def data_formatada():
    data_hora_utc = datetime.utcnow()
    fuso = pytz.timezone('America/Sao_Paulo')
    data_hora = data_hora_utc.replace(tzinfo=pytz.utc).astimezone(fuso)
    
    return data_hora.strftime('%Y-%m-%d %H:%M:%S')