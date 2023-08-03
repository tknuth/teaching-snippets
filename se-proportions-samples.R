# Eine (fiktive) Befragung, ob eine Reparaturpflicht für Elektrogeräte eingeführt
# werden sollte, antworten 85% der Bevölkerung mit Ja. Wie sicher ist die Richtigkeit
# dieses Wertes? Wie hängt der Grad des Vertrauens von der Stichprobengröße ab?

library(tidyverse)

set.seed(1)

p <- 0.85

# Wir tun so, als wäre der wahre Anteil der Befürwortung einer Reparaturpflicht 85%
# und simulieren eine Befragung von 100 Personen. Den wahren Wert kennt man
# in einer echten Befragung natürlich nicht, sondern er wird geschätzt.
x <- rbinom(100, 1, p)

# In unserer Stichprobe befürworten 87% der Befragten eine Reparaturpflicht.
# Diese Abweichung entsteht dadurch, dass wir zufällig Menschen befragt haben,
# die tendenziell etwas stärker für die Förderung von Solarenergie sind.
mean(x)

# Die folgende Zeile müssen Sie zu diesem Zeitpunkt nicht verstehen!
ask_people <- function(number_of_samples, sample_size) {
  map_dbl(1:number_of_samples, ~mean(rbinom(sample_size, 1, p)))
}

# Für die Funktion ask_people gilt:
# 1) Wir führen number_of_samples Befragungen durch
# 2) Bei jeder Befragung befragen wir sample_size Personen
# 3) In der Bevölkerung ist der Anteil der Befürwortung bei 85%
# 4) Für jede der Befragungen berechnen wir den empirischen Anteil der Befürwortung
ratios <- ask_people(10000, 100)

# Wir zeichnen das Histogramm der Befürwortungsanteile pro Befragung
hist(ratios)

# Wir können auch berechnen, wie stark der Anteil variiert
# Diese Standardabweichung beträgt 0.0359.
sd(ratios)

# Wir können diesen Wert aber auch theoretisch berechnen mit der Formel:
# SE_p = sqrt(p * (1 - p) / n)
# Der Standardfehler beträgt 0.0357.
sqrt(p * (1 - p) / 100)

# Wir haben viele Befragungen durchgeführt und die Standardabweichung der Anteile
# gemessen. Dies nennt man auch den Standardfehler. Der Standardfehler ist die
# Standardabweichung der Schätzstatistik.

# In der Praxis führt man natürlich nur eine Befragung durch und schätzt dann den
# Standardfehler mit der oben angegebenen Formel.
