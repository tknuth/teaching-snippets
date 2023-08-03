set.seed(5195112)

# sample a proportion of an experiment with n trials and a given success rate
sampleBinom <- function(n) {
  mean(rbinom(n, 1, 0.87))
}

# plot how the proportion changes with larger sample sizes
x <- 1:10000
y <- sapply(x, sampleBinom)
plot(x, y)

# what can be inferred comparing the first (low n) and last (high n) elements?
hist(head(y, 1000), breaks=10)
hist(tail(y, 1000), breaks=10)

