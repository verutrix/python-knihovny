# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/promitani

def prevod(vstup):
    result = []
    result = [str(round(delka / 60)) + ":" + str(delka % 60) for delka in vstup]

