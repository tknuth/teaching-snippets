set.seed(1)

plot_sse <- function(x, y) {
  plot(x, y)
  model <- lm(y ~ x)
  r <- cor(x, y)
  m = sd(y) / sd(x) * r
  b = mean(y) - m * mean(x)
  abline(model, col = "red")
  abline(h = mean(y), col = "blue")
  for (i in 1:length(x)) {
    lines(c(x[i], x[i]), c(b + m * x[i], y[i]))
  }
  points(x, y, pch = 21, bg = "white")
}

plot_ssr <- function(x, y) {
  plot(x, y)
  model <- lm(y ~ x)
  r <- cor(x, y)
  m = sd(y) / sd(x) * r
  b = mean(y) - m * mean(x)
  abline(model, col = "red")
  abline(h = mean(y), col = "blue")
  for (i in 1:length(x)) {
    lines(c(x[i], x[i]), c(b + m * x[i], mean(y)))
  }
  points(x, y, pch = 21, bg = "white")
}

plot_sst <- function(x, y) {
  plot(x, y)
  model <- lm(y ~ x)
  r <- cor(x, y)
  m = sd(y) / sd(x) * r
  b = mean(y) - m * mean(x)
  abline(model, col = "red")
  abline(h = mean(y), col = "blue")
  for (i in 1:length(x)) {
    lines(c(x[i], x[i]), c(mean(y), y[i]))
  }
  points(x, y, pch = 21, bg = "white")
}

plot_y <- function(x, y) {
  plot(rep(1, length(y)), y)
  lines(c(0.6, 1.4), c(mean(y), mean(y)), pch = 19, col = "red")
}

plot_mean <- function(x, y) {
  plot(x, y)
  model <- lm(y ~ x)
  abline(model, col = "red")
  lines(c(0, 100), c(mean(y), mean(y)), pch = 19, col = "blue")
}

# Wir erstellen Testdaten, die sich für eine lineare Regression eignen.
x <- 1:100
y <- x + rnorm(x, sd = 15)
# y <- x + rnorm(x, sd = 5)
# y <- x + rnorm(x, sd = 150)

plot_y(x, y)
plot_mean(x, y)
plot_sse(x, y)
plot_ssr(x, y)
plot_sst(x, y)
