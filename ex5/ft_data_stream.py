
import random
from typing import Generator

PLAYERS = [
    "bob",
    "alice",
    "dylan",
    "charlie"
]

ACTIONS = [
    "run",
    "eat",
    "sleep",
    "grab",
    "move",
    "climb",
    "swim",
    "use",
    "release"
]


def gen_event() -> Generator[tuple[str, str], None, None]:

    while True:

        player = random.choice(PLAYERS)
        action = random.choice(ACTIONS)
        yield (player, action)


def consume_event(events: list[tuple[str, str]]
                  ) -> Generator[tuple[str, str], None, None]:

    while events:

        i = random.randint(0, len(events) - 1)
        event = events.pop(i)
        yield event


if __name__ == '__main__':
    print("=== Game Data Stream Processor ===")

    events = gen_event()

    for i in range(1000):

        player, action = next(events)
        print(f"Event {i}: Player {player} did action {action}")

    event_list = []

    for i in range(10):
        event_list.append(next(events))
    print(f"Built list of 10 events: {event_list}")

    consume_ev = consume_event(event_list)
    for event in consume_ev:

        print(f"Got event from list: {event}")
        print(f"Remains in list: {event_list}")
