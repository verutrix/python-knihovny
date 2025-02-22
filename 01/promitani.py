# https://kodim.cz/czechitas/uvod-do-progr-2/bonusy/cykly-2/list-comprehension/promitani
import math

def prevod(vstup):
    return [f"{math.floor(delka / 60)}:{delka % 60:02d}" for delka in vstup]
    