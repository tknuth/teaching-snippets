# ---
# jupyter:
#   jupytext:
#     formats: ipynb,py:percent
#     text_representation:
#       extension: .py
#       format_name: percent
#       format_version: '1.3'
#       jupytext_version: 1.16.1
#   kernelspec:
#     display_name: Python 3 (ipykernel)
#     language: python
#     name: python3
# ---

# %% [markdown]
# ### Allgemeines
#
# - Relationale Datenbanken (SQL) sind Mengen aus Tupeln.
# - Die Reihenfolge der Einträge ist unerheblich.
# - Nichtrelationale Datenbanken (NoSQL) speichern z.B. Dokumente oder Schlüssel-Wert-Paare.
#
# ### Normalformen relationaler Datenbanken
#
# - 1. NF: Die Werte sind atomar.
# - 2. NF: Alle nicht-primären Attribute hängen vom gesamten Primärschlüssel ab.
# - 3. NF: Kein nicht-primäres Attribut hängt transitiv von einem anderen ab.
# - 4. NF: Mehrwertige Abhängigkeiten dürfen nur auf einem Kandidatenschlüssel basieren.
# - 5. NF: Eine Tabelle kann ohne Informationsverlust nicht weiter zerlegt werden.

# %%
import pandas as pd

# %%
# Verletzung der 1. NF
# Die Werte im Inventar sind nicht atomar.

pd.DataFrame(
    {
        "player_name": ["Aragon", "Elaine", "Borin"],
        "inventory": [
            "1 Schwert, 1 Schild",
            "1 Stab, 5 Potions, 2 Books",
            "1 Axt, 1 Helm, 1 Rüstung, 2 Schuhe",
        ],
    }
)

# %%
# Verletzung der 1. NF
# Die inhaltliche Bedeutung der Spalten überschneidet sich.
# Die maximale Spaltenanzahl hängt von der Größe der Inventare ab.

pd.DataFrame(
    {
        "player_name": ["Aragon", "Elaine", "Borin"],
        "item1_name": ["Schwert", "Stab", "Axt"],
        "item1_quantity": [1, 1, 1],
        "item2_name": ["Schild", "Trank", "Helm"],
        "item2_quantity": [1, 5, 1],
        "item3_name": ["Buch", "Rüstung", None],
        "item3_quantity": [2, 1, None],
        "item4_name": ["Schuhe", None, None],
        "item4_quantity": [2, None, None],
    }
)

# %%
# 1. NF erfüllt

inventories = pd.DataFrame(
    {
        "player_name": [
            "Aragon",
            "Aragon",
            "Elaine",
            "Elaine",
            "Elaine",
            "Borin",
            "Borin",
            "Borin",
            "Borin",
        ],
        "item_name": [
            "Schwert",
            "Schild",
            "Stab",
            "Trank",
            "Rune",
            "Axt",
            "Helm",
            "Rüstung",
            "Schuhe",
        ],
        "item_quantity": [
            1,
            1,
            1,
            5,
            2,
            1,
            1,
            1,
            2,
        ],
    }
)

inventories

# %%
# 2. NF verletzt
# Der Primärschlüssel ist `player_name` und `item_name`, aber
# die Spalte `player_level` hängt funktional nur von `player_name` ab.
# Es können Inkonsistenzen beim Löschen oder Ändern entstehen.

df = pd.DataFrame(
    {
        "player_name": [
            "Aragon",
            "Aragon",
            "Elaine",
            "Elaine",
            "Elaine",
            "Borin",
            "Borin",
            "Borin",
            "Borin",
        ],
        "player_level": [
            7,
            7,
            8,
            8,
            8,
            3,
            3,
            3,
            3,
        ],
        "item_name": [
            "Schwert",
            "Schild",
            "Stab",
            "Trank",
            "Rune",
            "Axt",
            "Helm",
            "Rüstung",
            "Schuhe",
        ],
        "item_quantity": [
            1,
            1,
            1,
            5,
            2,
            1,
            1,
            1,
            2,
        ],
    }
)

df

# %%
# Inkonsistenz beim Löschen
# Aragon hat keine Items mehr, welches Level ist sein Charakter?

df[df.player_name != "Aragon"]

# %%
# Inkonsistenz beim Ändern
# Das Level von Aragon ist uneindeutig, z.B. durch ein fehlerhaftes Update.

df.iloc[0, 1] = 8
df

# %%
players = pd.DataFrame(
    {
        "player_name": ["Aragon", "Elaine", "Borin"],
        "player_level": [7, 8, 3],
    }
)

players

# %%
# 3. NF verletzt
# Spalten mit Datumswerten hängen voneinander ab.

players = pd.DataFrame(
    {
        "player_name": ["Aragon", "Elaine", "Borin"],
        "player_level": [7, 8, 3],
        "player_birth_date": ["1999-01-09", "1995-12-23", "2002-10-07"],
        "player_birth_day": ["Samstag", "Samstag", "Montag"],
    }
)

players

# %%
# 4. NF verletzt
# Verschiedene mögliche Farben führen zu Redundanz der Gewichtsangaben.

pd.DataFrame(
    {
        "item_name": [
            "Schwert",
            "Schild",
            "Stab",
            "Trank",
            "Trank",
            "Rune",
            "Axt",
            "Helm",
            "Rüstung",
            "Schuhe",
            "Schuhe",
        ],
        "item_color": [
            "silbern",
            "schwarz",
            "braun",
            "rot",
            "blau",
            "schwarz",
            "silbern",
            "silbern",
            "beige",
            "schwarz",
            "braun",
        ],
        "item_weight": [
            4,
            7,
            2,
            1,
            1,
            1,
            5,
            4,
            5,
            1,
            1,
        ],
    }
)

# %%
# 5. NF verletzt
# Inkonsistenzen entstehen durch implizite Regeln.

clothes = pd.DataFrame(
    {
        "item_name": [
            "Helm",
            "Hut",
            "Handschuhe",
            "Hemd",
            "Schuhe",
            "Schuhe",
        ],
        "item_color": [
            "silbern",
            "braun",
            "schwarz",
            "weiß",
            "braun",
            "schwarz",
        ],
        "item_type": [
            "schwer",
            "leicht",
            "leicht",
            "leicht",
            "mittel",
            "schwer",
        ],
    }
)

clothes

# %%
# Borin bevorzugt silberne/schwarze mittlere bis schwere Rüstung.
# Aragon bevorzugt braune/weiße leichte bis mittlere Rüstung.

compatible_items = pd.DataFrame(
    {
        "player_name": [
            "Borin",
            "Borin",
            "Aragon",
            "Aragon",
            "Aragon",
        ],
        "item_name": [
            "Helm",
            "Schuhe",
            "Hut",
            "Hemd",
            "Schuhe",
        ],
        "item_color": [
            "silbern",
            "schwarz",
            "braun",
            "weiß",
            "braun",
        ],
        "item_type": [
            "schwer",
            "mittel",
            "leicht",
            "leicht",
            "mittel",
        ],
    }
)

compatible_items

# %%
# Nichtrelationales Schema

players_inventory = {
    "Aragon": {
        "items": [
            {
                "name": "Schwert",
                "description": "Ein robustes Schwert.",
            },
            {
                "name": "Schild",
                "description": "Ein runder Schild.",
            },
        ]
    },
    "Elaine": {
        "items": [
            {
                "name": "Stab",
                "description": "Ein magischer Stab.",
            },
            {
                "name": "Trank",
                "description": "Ein kleiner Heiltrank.",
            },
            {
                "name": "Rune",
                "description": "Eine magische Rune.",
            },
        ]
    },
    "Borin": {
        "items": [
            {
                "name": "Axt",
                "description": "Eine schwere Axt.",
            },
            {
                "name": "Helm",
                "description": "Ein stabiler Helm.",
            },
            {
                "name": "Rüstung",
                "description": "Eine schwere Plattenrüstung.",
            },
            {
                "name": "Schuhe",
                "description": "Stabile Stiefel.",
            },
        ]
    },
}
