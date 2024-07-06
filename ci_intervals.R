set.seed(1)

# Diesen Code müssen Sie nicht verstehen!
plot_intervals <- function(sample_size, number_of_samples) {
  p <- 0.5
  w <- 1:number_of_samples
  plot(c(0.4, 0.6), c(1, length(w)), type = "n")
  abline(v = p)
  cnt <- 0
  for (i in w) {
    v <- rbinom(sample_size, 1, p)
    se <- sqrt(mean(v) * (1 - mean(v)) / sample_size)
    upper <- mean(v) + se * qnorm(.975)
    lower <- mean(v) + se * qnorm(.025)
    covered <- p >= lower & p <= upper
    color <- ifelse(covered, 1, 2)
    if (!covered)
      cnt <- cnt + 1
    lines(c(lower, upper), c(i, i), col = color)
  }
  print(cnt / number_of_samples)
}

# Der Plot zeigt die Konfidenzintervalle, die auf Basis wiederholt gebildeter
# Stichproben (number_of_samples) entstehen. Ein Konfidenzintervall sagt, dass
# der wahre Wert mit einer Wahrscheinlichkeit von alpha (Konfidenzniveau)
# innerhalb des berechneten Intervalls liegt. Das bedeutet aber auch, dass das
# Konfidenzintervall den wahren Wert manchmal gar nicht erfasst!
# Im Beispiel ist der wahre Wert 50%. Die rot markierten Linien zeigen,
# wenn das Konfidenzintervall diesen Wert aufgrund der Stichprobe mit zufällig
# besonders hohen oder niedrigen Werten gar nicht beinhaltet.
# Das ist das Risiko, das durch das Konfidenzniveau angegeben wird.
plot_intervals(1000, 100)
