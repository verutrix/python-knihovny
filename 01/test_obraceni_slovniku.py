from obraceni_slovniku import obrat_slovnik


def test_obrat_slovnik():
    vstup = {"Jablko": "Apple", "Knoflík": "Button", "Myš": "Mouse"}
    vystup = {"Apple": "Jablko", "Button": "Knoflík", "Mouse": "Myš"}
    assert obrat_slovnik(vstup) == vystup


def test_obrat_slovnik_prazdny():
    assert obrat_slovnik({}) == {}
