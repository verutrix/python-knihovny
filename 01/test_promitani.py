# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/promitani

from promitani import prevod


def test_ukazka():
    vstup = [136, 105, 82]
    vystup = ['2:16', '1:45', '1:22']
    assert prevod(vstup) == vystup


def test_prazdny():
    assert prevod([]) == []


def test_specialni():
    vstup = [1, 61]
    vystup = ['0:01', '1:01']
    assert prevod(vstup) == vystup
