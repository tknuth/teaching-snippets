set.seed(1)

# Wir erstellen Testdaten, die sich für eine lineare Regression eignen.
x <- 1:100
y <- x + rnorm(x, sd = 10)
plot(x, y)

# Lineare Regression anwenden
model <- lm(y ~ x)

# Linie plotten
abline(model, col = "red")

# Zusammenfassung des Modells ausgeben
summary(model)

# Die Geradengleichung lautet y_hat = 1.31666 + 0.99549 * x.
# Wenn sich also der x-Wert um 1 erhöht, steigt y_hat um 0.99549.
# Die Residuen der Quantile sind relativ symmetrisch um die Mitte verteilt.
# Vgl. hierzu Q1 und Q3 sowie min und max.

# Das Bestimmtheitsmaß R^2 beträgt 0.9118, ein hoher Wert. Das lineare Modell
# kann 91.18% der Streuung um den y-Mittelwert erklären.

# Da wir Hypothesentests bisher noch nicht bearbeitet haben, können wir diese
# folgenden beiden Werte bis jetzt nur eingeschränkt interpretieren.

# Die x-Variable ist signifikant (***) mit einem p-Wert von 2e-16,
# d.h. mit großer Wahrscheinlichkeit nicht null.

# Der F-Test ergibt einen p-Wert von 2.2e-16 und zeigt ein signifikantes Modell an.
# Der p-Wert des F-Tests ist die Wahrscheinlichkeit, dass alle Koeffizienten tatsächlich null sind.
# Hinweis: Hier gibt es nur den einen Koeffizienten x.
