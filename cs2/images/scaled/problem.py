# Scale an image to be twice as big

from PIL import Image

# Load input image
im = Image.open("bird.png")

# Make blank output image with twice the width and height of the original
output = Image.new(im.mode, (im.width * 2, im.height * 2))

for y in range(im.height):
  for x in range(im.width):
    (r, g, b) = im.getpixel((x, y))

    output.putpixel((x, y), (r, g, b))

# Save output image
output.save("scaled.png")
