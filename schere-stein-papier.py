import random

MOVES = ["Schere", "Stein", "Papier"]


def main():
    print("Schere, Stein, Papier")
    print()
    while True:
        choice = input("Wähle 1. Schere, 2. Stein oder 3. Papier: ")
        if choice in ["1", "2", "3"]:
            player_move = MOVES[int(choice) - 1]
            print()
            print(f"Du wählst {player_move}.")
            break
        print("Ungültige Eingabe, versuche es erneut.")
        print()

    computer_move = random.choice(MOVES)
    print(f"Der Computer wählt {computer_move}.")
    print()

    d = (MOVES.index(player_move) - MOVES.index(computer_move)) % 3
    if d == 0:
        print("Unentschieden!")
    if d == 1:
        print("Du gewinnst!")
    if d == 2:
        print("Du verlierst!")


if __name__ == "__main__":
    main()
