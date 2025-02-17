from mnozina_zaokrouhlenych import mnozina_zaokrouhlenych


def test_mnozina_zaokrouhlenych():
    vstup = {1, 1.1, 1.2, 1.9, 2, 2.4, 10, 10.9}
    vystup = {1, 2, 10, 11}
    assert mnozina_zaokrouhlenych(vstup) == vystup


def test_mnozina_prazdna():
    assert mnozina_zaokrouhlenych(set()) == set()


def test_seznam():
    vstup = [0, 0, 0, 0, 0.1, 1.11, -1.1, -1, -0.9]
    vystup = {-1, 0, 1}
    assert mnozina_zaokrouhlenych(vstup) == vystup
