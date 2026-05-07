
import random


LIST_ACHIEVEMENTS = {
    "Crafting Genius",
    "World Savior",
    "Master Explorer",
    "Unstoppable",
    "Collector Supreme",
    "Untouchable",
    "Boss Slayer",
    "Strategist",
    "Unstoppable",
    "Speed Runner",
    "Survivor",
    "Treasure Hunter",
    "First Steps",
    "Sharp Mind"
}


def gen_player_achievements() -> set[str]:

    amount = random.randint(5, 9)

    return set(random.sample(list(LIST_ACHIEVEMENTS), amount))


def gen_player() -> dict[str, set[str]]:
    return {
        "Alice": gen_player_achievements(),
        "Bob": gen_player_achievements(),
        "Charlie": gen_player_achievements(),
        "Dylan": gen_player_achievements()
    }


if __name__ == '__main__':

    print("=== Achievement Tracker System ===\n")

    players = gen_player()

    for name, achievements in players.items():
        print(f"Player {name}: {achievements}\n")

    list_achievements = set.union(*players.values())
    print(f"All distinct achievements: {list_achievements}\n")

    common = set.intersection(*players.values())
    print(f"Common achievements: {common}\n")

    for name, achievements in players.items():

        others = []

        for other_name, other_achievements in players.items():
            if other_name != name:
                others.append(other_achievements)

        difference = set.difference(achievements, *others)

        print(f"Only {name} has: {difference}")

    print()

    for name, achievements in players.items():
        missing = set.difference(
            LIST_ACHIEVEMENTS,
            achievements
        )

        print(f"{name} is missing: {missing}")
