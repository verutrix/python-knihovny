# Napiš funkci, která vrátí ze iterovatelného vstupu množinu zaokrouhlených hodnot

vstup = {1, 1.1, 1.2, 1.9, 2, 2.4, 10, 10.9}

def mnozina_zaokrouhlenych(vstup):
    return {round(hodnota) for hodnota in vstup}

print(mnozina_zaokrouhlenych(vstup))