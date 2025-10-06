count = 0


def on_gesture_shake():
    global count
    count = randint(0, 2)
    if count == 0:
        basic.show_string("R")
    elif count == 1:
        basic.show_string("P")
    else:
        basic.show_string("S")


input.on_gesture(Gesture.SHAKE, on_gesture_shake)
