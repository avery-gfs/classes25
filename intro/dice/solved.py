count = 0


def on_gesture_shake():
    global count
    count = randint(1, 6)
    if count == 1:
        basic.show_leds(
            """
            . . . . .
            . . . . .
            . . # . .
            . . . . .
            . . . . .
            """
        )
    elif count == 2:
        basic.show_leds(
            """
            . . . . .
            . . . # .
            . . . . .
            . # . . .
            . . . . .
            """
        )
    elif count == 3:
        basic.show_leds(
            """
            . . . . .
            . . . # .
            . . # . .
            . # . . .
            . . . . .
            """
        )
    elif count == 4:
        basic.show_leds(
            """
            . . . . .
            . # . # .
            . . . . .
            . # . # .
            . . . . .
            """
        )
    elif count == 5:
        basic.show_leds(
            """
            . . . . .
            . # . # .
            . . # . .
            . # . # .
            . . . . .
            """
        )
    else:
        basic.show_leds(
            """
            . . . . .
            . # . # .
            . # . # .
            . # . # .
            . . . . .
            """
        )


input.on_gesture(Gesture.SHAKE, on_gesture_shake)
