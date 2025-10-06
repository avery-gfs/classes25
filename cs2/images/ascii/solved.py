from PIL import Image

im = Image.open("dali.webp")

width = 100
height = round(width * im.height / im.width / 2)

im = im.convert("L").resize((width, height))

symbols = "BEOec<+:~-'``   "[::-1]  # Reverse string for dark-on-light text

for y in range(im.height):
    row = ""

    for x in range(im.width):
        l = im.getpixel((x, y))
        index = round(l / 255 * (len(symbols) - 1))
        row += symbols[index]

    print(row)
