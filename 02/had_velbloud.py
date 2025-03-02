"""Napište program, který dostane na příkazovém řádku název proměnné v hadí notaci a vrátí tentýž název zapsaný ve velbloudí notaci.

Příklad:

python had-velbloud.py had_honi_velblouda
hadHoniVelblouda"""
import sys

zmena = sys.argv[1]
zmena = zmena.split("_")
zmena = [w.capitalize() for w in zmena]

result = "".join(zmena)
print(result)



