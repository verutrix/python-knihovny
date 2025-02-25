# Napiš funkci, která vrátí ze iterovatelného vstupu množinu zaokrouhlených hodnot

def mnozina_zaokrouhlenych(vstup):
    return {round(hodnota) for hodnota in vstup}