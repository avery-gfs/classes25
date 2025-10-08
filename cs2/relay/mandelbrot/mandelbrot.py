from PIL import Image

minX = -2.1
maxX = 0.9

minY = -1.3
maxY = 1.3

scale = 500

width = round((maxX - minX) * scale)
height = round((maxY - minY) * scale)

maxIters = 100

output = Image.new("RGB", (width, height))


def getIters(c):
    z = 0

    for i in range(maxIters + 1):
        if abs(z) > 2:
            return i

        z = z**2 + c

    return 0


print("rendering")

for y in range(height):
    for x in range(width):
        iters = getIters(x / scale + minX + (y / scale + minY) * 1j)
        r = round(255 * (iters / maxIters) ** 0.5)
        output.putpixel((x, y), (r, 0, 0))

output.save("fractal.png")
print("finshed")
