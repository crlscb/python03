
import random

PLAYER_NAMES = [
    "Alice",
    "bob",
    "Charlie",
    "dylan",
    "Emma",
    "Gregory",
    "john",
    "kevin",
    "Liam"
]

if __name__ == '__main__':
    print("=== Game Data Alchemist ===\n")

    print(f"Initial list of players: {PLAYER_NAMES}\n")

    capitalized = [
        player.capitalize()
        for player in PLAYER_NAMES
    ]
    print(f"New list with all names capitalized: {capitalized}")

    only_capitalized = [
        player
        for player in PLAYER_NAMES
        if player[0].isupper()
    ]
    print(f"New list of capitalized names only: {only_capitalized}\n")

    scores = {
        player: random.randint(0, 1000)
        for player in capitalized
    }
    print(f"Score dict: {scores}")

    average = round(sum(scores.values()) / len(scores), 2)
    print(f"Score average is {average}")

    high_scores = {
        player: score
        for player, score in scores.items()
        if score > average
    }
    print(f"High scores: {high_scores}")
