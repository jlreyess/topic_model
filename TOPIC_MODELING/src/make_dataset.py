
import re as re

def clean(df) :
    # Convertir a una lista
    data = df.content.values.tolist()
    # Eliminar emails
    data = [re.sub(r'\S*@\S*\s?', '', sent) for sent in data]
    # Eliminar newlines
    data = [re.sub(r'\s+', ' ', sent) for sent in data]
    # Eliminar comillas
    data = [re.sub(r"\'", "", sent) for sent in data]

    return data




