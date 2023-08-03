set.seed(1)

# Wir erstellen 100 normalverteilte Werte mit Mittelwert 170cm
# und Standardabweichung 30cm als Verteilung der Körpergrößen.
x <- rnorm(100, mean = 170, sd = 30)

# Histogramm zeichnen
hist(x)

# Quantile berechnen, in diesem Beispiel Quartile
percentages <- seq(0, 1, 0.25)
quantile(x, percentages)

# 25% der Personen sind kleiner als 156cm.
# 50% der Personen sind kleiner als 174cm.
# 75% der Personen sind kleiner als 191cm.
