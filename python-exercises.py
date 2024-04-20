#!/usr/bin/env python
# coding: utf-8
# %%
# Die for-Schleife gibt eine Liste mit den geraden Zahlen aus.
# Verwenden Sie while statt for.

values = [1, 9, 2, 7, 3, 5, 8, 4]
result = []

for i in values:
    if i % 2 == 0:
        result.append(i)

result

# %%
# Die while-Schleife gibt die Zahlen 2**i für natürliche Zahlen i aus.
# Verwenden Sie for statt while.

i = 1
result = []

while 2**i < 100:
    result.append(2**i)
    i += 1

result


# %%
# Schreiben Sie eine Funktion,
# die einen "Slug" generiert,
# d.h. eine lesbare URL eines Titels.
# Nutzen Sie die String-Methoden.
# https://devdocs.io/python~3.12/library/stdtypes#str


def slug(s): ...


slug("Programmierung mit Python")  # programmierung-mit-python


# %%
# Schreiben Sie eine Funktion,
# welche Grad Celsius in Grad Fahrenheit und Kelvin umrechnet.
# Formel: x°C * 9/5 + 32 = y°F
# Geben Sie einen String aus, der die Werte für alle Formate nennt.
def temperature(c): ...


temperature(0)  # "0°C sind 32°F und 273K."

# %%
# Schreiben Sie eine Funktion,
# mit der Sie einen Würfel simulieren.
# Sie können angeben, wie viele Seiten der Würfel hat.
# Nutzen Sie `random.randint()`.

import random


def dice(n=6): ...


dice(12)  # Zahl zwischen 1 und 12


# %%
# Schreiben Sie eine Funktion,
# welche die ersten n Elemente einer Liste ausgibt.


def head(l, n=1): ...


head([1, 2, 3, 4, 5], n=3)  # [1, 2, 3]


# %%
# Schreiben Sie eine Funktion,
# welche die letzten n Elemente einer Liste ausgibt.


def tail(l, n=1): ...


tail([1, 2, 3, 4, 5], n=3)  # [3, 4, 5]


# %%
# Schreiben Sie eine Funktion,
# welche Angaben für ein Literaturverzeichnis erstellt.


def cite(author, title, year): ...


cite("Meyer", "Informatik", 2012)  # "Meyer (2012): Informatik."

# Erweitern Sie die Funktion,
# sodass auch eine Liste aus Autorinnen und Autoren übergeben werden kann.

cite(["Meyer", "Müller"], "Statistik", 2010)  # "Meyer und Müller (2010): Statistik."


# %%
# Schreiben Sie eine Funktion,
# um den Abstand zwischen zwei Buchstaben im Alphabet zu berechnen.


def delta(a, b): ...


delta("d", "h")  # 4
delta("c", "a")  # -2
