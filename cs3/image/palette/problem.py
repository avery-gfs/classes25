from PIL import Image
import math

# Load input image
im = Image.open("bird.png")

# Make blank output image with same dimension as the original
output = Image.new(im.mode, im.size)

# Calculate color distance between two colors
# https://en.wikipedia.org/wiki/Color_difference

def distance(c1, c2):
	# Your code goes here
	pass

# https://rgbcolorpicker.com/
# https://lospec.com/palette-list/endesga-16

endesga16 = [
    (228, 166, 114),
    (184, 111, 80),
    (116, 63, 57),
    (63, 40, 50),
    (158, 40, 53),
    (229, 59, 68),
    (251, 146, 43),
    (255, 231, 98),
    (99, 198, 77),
    (50, 115, 69),
    (25, 61, 63),
    (79, 103, 129),
    (175, 191, 210),
    (255, 255, 255),
    (44, 232, 244),
    (4, 132, 209),
]

for y in range(im.height):
	for x in range(im.width):
		# Your code goes here
		
		pass

# Save output image
output.save("palette.png")
