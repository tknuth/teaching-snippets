# Wir berechnen zuerst eine Punktschätzung. Allerdings wissen wir, dass der wahre
# Anteil mit dieser Stichprobe nur geschätzt werden kann!
relevant <- 24
n <- 200
p_hat <- relevant / n

# Die Unsicherheit bestimmen wir mit dem Standardfehler.
# Dieser beträgt 0.023.
se <- sqrt(p_hat * (1 - p_hat) / n)

# Aber was sagt uns dieser Wert?
# Dank des zentralen Grenzwertsatzes wissen wir, dass p_hat
# einer Normalverteilung folgt. Daher können wir aus der Normalverteilung ablesen,
# wie groß die Wahrscheinlichkeit ist, dass eine beliebige Stichprobe wie die,
# die wir gesammelt haben, innerhalb eines Fensters um p_hat liegt.

# Bei der Standardnormalverteilung liegen 84% der Daten unterhalb
# einer Standardabweichung über dem Mittelwert.
pnorm(1)

# Bei der Standardnormalverteilung liegen 68% der Daten innerhalb
# plus/minus einer Standardabweichung um den Mittelwert (bzw. Anteil).
# Hier ziehen wir sozusagen von beiden Seiten die Ränder ab.
1 - 2 * (1 - pnorm(1))

# Mit einem Konfidenzintervall können wir berechnen, in welchem Intervall sich
# der wahre Wert p mit einer bestimmten Wahrscheinlichkeit befindet.
# Wir wissen, dass bei der Standardnormalverteilung 95% der Daten innerhalb
# von -1.96 bis 1.96 liegen. Man beachte, dass bei einem 95%-Konfidenzintervall
# 2.5% auf beiden Seiten der Verteilung liegen.
z_crit <- qnorm(0.025)

# Wir berechnen das Konfidenzintervall. Mit einer Wahrscheinlichkeit von 95%
# befindet sich der wahre Wert innerhalb von 7.5% und 16.5%.
p_hat + z_crit * se
p_hat - z_crit * se

# Selbst wenn der wahre Anteil p = 10% ist, ändert sich nicht viel am Standardfehler.
# Man erinnere: Der Standardfehler berechnet sich eigentlich mit p, aber meistens
# haben wir nur p_hat und verwenden dies näherungsweise.
# Standardfehler mit p_hat: 0.023
# Standardfehler mit p: 0.021
p <- 0.1
sqrt(p * (1 - p) / n)
