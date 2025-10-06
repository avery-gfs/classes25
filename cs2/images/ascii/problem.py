from PIL import Image

im = Image.open("dali.webp")

width = 100
height = round(width * im.height / im.width / 2)

im = im.convert("L").resize((width, height))

for y in range(im.height):
    row = ""

    for x in range(im.width):
        pass  # Your code goes here

    print(row)
