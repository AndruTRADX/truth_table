import pandas as pd

# Definición de la función para imprimir el estado de los LEDs
def print_leds(a1, b1, c1, d1, e1, f1, g1, a2, b2, c2, d2, e2, f2, g2):
    # Crear el formato de los LEDs para el primer display
    display1 = [
        f" {a1} ",
        f"{f1} {b1}",
        f" {g1} ",
        f"{e1} {c1}",
        f" {d1} "
    ]

    # Crear el formato de los LEDs para el segundo display
    display2 = [
        f" {a2} ",
        f"{f2} {b2}",
        f" {g2} ",
        f"{e2} {c2}",
        f" {d2} "
    ]

    # Imprimir el estado de los LEDs para ambos displays alineados en una columna
    print("Display 1 and Display 2:")
    for line1, line2 in zip(display1, display2):
        print(f"{line1}  {line2}")

# Valores corregidos según los patrones descritos

values = [ 
#   p1; p2; p3; p4; a1; b1; c1; d1; e1; f1; g1; a2; b2; c2; d2; e2; f2; g2;
    "0;  0;  0;  0;  1;  1;  1;  1;  1;  1;  0;  1;  1;  1;  1;  1;  1;  0",  # 0
    "0;  0;  0;  1;  1;  1;  1;  1;  1;  1;  0;  0;  1;  1;  0;  0;  0;  0",  # 1
    "0;  0;  1;  0;  1;  1;  1;  1;  1;  1;  0;  1;  1;  0;  1;  1;  0;  1",  # 2
    "0;  0;  1;  1;  1;  1;  1;  1;  1;  1;  0;  1;  1;  1;  1;  0;  0;  1",  # 3
    "0;  1;  0;  0;  1;  1;  1;  1;  1;  1;  0;  0;  1;  1;  0;  0;  1;  1",  # 4
    "0;  1;  0;  1;  1;  1;  1;  1;  1;  1;  0;  1;  0;  1;  1;  0;  1;  1",  # 5
    "0;  1;  1;  0;  1;  1;  1;  1;  1;  1;  0;  1;  1;  1;  1;  1;  0;  1",  # 6
    "0;  1;  1;  1;  1;  1;  1;  1;  1;  1;  0;  1;  1;  1;  0;  0;  0;  1",  # 7
    "1;  0;  0;  0;  1;  1;  1;  1;  1;  1;  0;  1;  1;  1;  1;  1;  1;  1",  # 8
    "1;  0;  0;  1;  1;  1;  1;  1;  1;  1;  0;  1;  1;  1;  0;  0;  1;  1",  # 9
    "1;  0;  1;  0;  0;  1;  1;  0;  0;  0;  0;  1;  1;  1;  1;  1;  1;  0",  # 10
    "1;  0;  1;  1;  0;  1;  1;  0;  0;  0;  0;  0;  1;  1;  0;  0;  0;  0",  # 11
    "1;  1;  0;  0;  0;  1;  1;  0;  0;  0;  0;  1;  1;  0;  1;  1;  0;  1",  # 12
    "1;  1;  0;  1;  0;  1;  1;  0;  0;  0;  0;  1;  1;  1;  1;  0;  0;  1",  # 13
    "1;  1;  1;  0;  0;  1;  1;  0;  0;  0;  0;  0;  1;  1;  0;  0;  1;  1",  # 14
    "1;  1;  1;  1;  0;  1;  1;  0;  0;  0;  0;  1;  0;  1;  1;  0;  1;  1"   # 15
]     

  
#   Convertir   los   valores a formato decimal
for value in values:
    p1, p2, p3, p4, a1, b1, c1, d1, e1, f1, g1, a2, b2, c2, d2, e2, f2, g2 = map(int, value.split(';'))
    print(f"Input: {p1}{p2}{p3}{p4}")
    print_leds(a1, b1, c1, d1, e1, f1, g1, a2, b2, c2, d2, e2, f2, g2)
    print()
