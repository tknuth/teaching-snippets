# Ein Bekannter behauptet, die Bevölkerung sei indifferent in Bezug auf die Bedeutung
# des Ausbaus des Schienennetzes zur Bewältigung der Klimaprobleme.
# Sie bezweifeln diese Aussage und befragen 100 Personen.
# 60% der Befragten halten den Ausbau für wichtig.
# Kann von einer statistisch signifikanten Tendenz gesprochen werden?

set.seed(1)

p_hat <- 0.60
n <- 100

# Wir definieren:
# H_0: p = 50%
# H_1: p != 50%
p_0 <- 0.5

# Die Daten sprechen dafür, dass p ungleich 50% ist, denn es ist recht
# unwahrscheinlich, dass 1000 Personen einen Anteil p_hat von 60% ergeben,
# wenn p tatsächlich 50% ist.

# Der Standardfehler ist 0.05.
# Man beachte, dass wir hier annehmen, dass der wahre Anteil p_0 ist.
# Später prüfen wir, inwieweit p_hat Anlass dazu gibt, H_0 zugunsten von H_1 zu verwerfen.
se <- sqrt(p_0 * (1 - p_0) / n)

# Wie viele Standardabweichungen ist unser p_hat von p_0 entfernt?
# z hat den Wert 2, d.h. es ist eher unwahrscheinlich, dass die vorliegenden
# Ergebnisse unter der Nullhypothese entstanden sind.
z <- (p_hat - p_0) / se

# Wie unwahrscheinlich dies ist, drückt der p-Wert als Wahrscheinlichkeit aus.
# Wir multiplizieren mit 2, da die Verteilung zwei Seiten hat.
# Das Ergebnis ist 4.5%, also verwerfen wir die Nullhypothese.
# Normalerweise verwendet man Signifikanzniveaus wie 1% oder 5%.
# Mit 1% ist unser Ergebnis nicht mehr signifikant.
2 * (1 - pnorm(z))

# Die beiden roten Punkte markieren, wo in der Standardnormalverteilung
# die ermittelten z-Werte liegen. Die Abbildung zeigt daher, wie äußerst
# unwahrscheinlich die erhaltenen Ergebnisse unter der Nullhypothese sind.
x <- seq(-10, 10, 0.01)
plot(x, dnorm(x), "l")
points(z, 0, pch = 18, col = "red")
points(-z, 0, pch = 18, col = "red")
