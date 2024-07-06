library(tidyverse)

set.seed(1)

n_vals <- c(10, 25, 50)
p_vals <- seq(0.1, 0.9, 0.2)

df <- as_tibble(expand.grid(n = n_vals, p = p_vals)) %>%
  mutate()

generateTable <- function(n, p) {
  as_tibble(expand.grid(
    n = n,
    p = p,
    value = map_dbl(1:50000, ~ mean(rbinom(n, 1, p)))
  ))
}

r <- tibble(n = numeric(0),
            p = numeric(0),
            value = numeric(0))

for (i in seq(nrow(df))) {
  n <- df$n[i]
  p <- df$p[i]
  r <- bind_rows(r, generateTable(n, p))
}

ggplot(r, aes(value)) +
  geom_histogram(aes(y = after_stat(count / sum(count))), binwidth = 0.02) +
  facet_grid(rows = vars(p), cols = vars(n)) +
  theme_minimal()
