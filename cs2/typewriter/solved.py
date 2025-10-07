# Credit to Mohammad for this idea

import time
import random


def display(message):
    for c in message:
        print(c, end="", flush=True)
        time.sleep(0.05 + 0.2 * random.random())
    print()


display(
    """
Hello world!

According to all known laws of aviation, there is no way a bee should be able to fly.
Its wings are too small to get its fat little body off the ground.
The bee, of course, flies anyway because bees don't care what humans think is impossible.
""".strip()
)
