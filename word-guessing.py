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

# %%
def contains(a, b):
    return a.lower() in b.lower()


def mask_letter(c, skip, mask):
    return mask if c.isalpha() and not contains(c, skip) else c


def mask_sentence(sentence, skip, mask):
    return ''.join([mask_letter(c, skip, mask) for c in sentence])


def play(sentence, max_mistakes=3, mask="#"):
    guesses = ""
    mistakes = 0
    masked = mask_sentence(sentence, "", mask)
    print("Willkommen zum Wörterraten!")

    while True:
        print(f"Du hast noch {max_mistakes - mistakes} Fehler frei.")
        print()
        print(masked)
        
        guess = input("Gib einen Buchstaben ein: ").strip()
        guesses += guess
        masked = mask_sentence(sentence, guesses, mask)

        if contains(guess, sentence):
            print(f"Ja, ein {guess} existiert.")
        else:
            print(f"Nein, ein {guess} existiert nicht.")
            mistakes += 1
        
        if mistakes > max_mistakes:
            print("Schade, du konntest den Satz nicht erraten.")
            break
            
        if not mask in masked:
            print("Glückwunsch, du hast gewonnen!")
            break

    print()
    print("Der Satz war: " + sentence)

sentence = "Wir lernen Python, das macht Spaß!"
play(sentence)
