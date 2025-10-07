def on_button_pressed_a():
    global count
    count += 1
    basic.show_number(count)


input.on_button_pressed(Button.A, on_button_pressed_a)

count = 0
count = 0
basic.show_number(count)
