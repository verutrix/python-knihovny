# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/promitani

def prevod(vstup):
    return [f"{(delka // 60)}:{delka % 60:02d}" for delka in vstup]
    