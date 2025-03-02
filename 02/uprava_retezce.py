"""Napište program, který dostane jako jeden parametr řetězec s mezerami (aby to fungovalo, musí být ten řetězec obalen v uvozovkách).
 Vypište tento řetězec tak, že mezery nahradíte za podtržítka.

python uprava_retezce.py "retezec s mezerami"
retezec_s_mezerami"""

import sys

retezec = sys.argv[1]
result = ""
for char in retezec:
    if char == " ":
        result += "_"
    else:
        result += char

print(result)

