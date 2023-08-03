set.seed(1)

x = seq(0, 10, 0.1)

y1 = (x - 3) ^ 2 - 4 + rnorm(length(x), mean = 0, sd = 1)
y2 = 3 * x + 10 + rnorm(length(x), mean = 0, sd = 2)
y3 = 3 * x + 10 + rnorm(length(x), mean = 0, sd = 20)
y4 = -3 * x + 10 + rnorm(length(x), mean = 0, sd = 5)

plot(x, y1)
plot(x, y2)
plot(x, y3)
plot(x, y4)

# Welches der oben dargestellten Daten haben den höchsten Korrelationskoeffizienten?
# Benutzen Sie den Befehl cor(x, y).
