import os




from ftfy import fix_text

def load_data(path):
    """
    Charger et corriger les données pour respecter les accents français.
    """
    input_file = os.path.join(path)
    with open(input_file, "r", encoding="utf-8") as f:
        data = f.read()
    
    # Réparer les anomalies d'encodage
    data = fix_text(data)
    
    return data.split("\n")
