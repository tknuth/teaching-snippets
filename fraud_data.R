library(tidyverse)

df <- tribble(
  ~Preis,    ~Kategorie,   ~Versandart, ~Betrug,
  "teuer",   "Elektronik", "Express",   "ja",
  "teuer",   "Elektronik", "Express",   "ja",
  "teuer",   "Elektronik", "Express",   "ja",
  "teuer",   "Elektronik", "normal",    "ja",
  "teuer",   "Elektronik", "normal",    "ja",
  "teuer",   "Elektronik", "normal",    "nein",
  "teuer",   "Kleidung",   "normal",    "nein",
  "teuer",   "Kleidung",   "Express",   "ja",
  "günstig", "Kleidung",   "normal",    "nein",
  "günstig", "Kleidung",   "normal",    "nein",
  "günstig", "Kleidung",   "normal",    "nein",
  "günstig", "Elektronik", "normal",    "nein",
  "günstig", "Elektronik", "normal",    "nein",
  "günstig", "Elektronik", "normal",    "nein",
  "günstig", "Elektronik", "Express",   "ja",
  "günstig", "Kleidung",   "Express",   "nein"
)

# Entropie
p <- 7/16
h <- -p * log2(p) - (1 - p) * log2(1 - p)
h

# Der Information Gain ist die Differenz zwischen der Entropie vor der Teilung
# und dem gewichteten Mittel der Entropien nach der Teilung.
