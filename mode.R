x <- rep(c(1, 1, 2, 3, 1, 5, 3, 4, 2, 3, 4, 5, 5, 5), 2)

# Tabelle der Häufigkeiten
table(x)

# Welchen Wert hat der Modus?
max(table(x))

# An welcher Position befindet sich der Modus?
which.max(tabulate(x))
