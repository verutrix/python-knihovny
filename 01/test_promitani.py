# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/promitani

from promitani import prevod

def test_prevod():
    vstup = [136, 105, 82]
    vystup = ['2:16', '1:45', '1:22']

    assert prevod(vstup) == vystup
