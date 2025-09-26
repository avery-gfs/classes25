print("CS 2 Info")

print(
    {
        "name": "Avery Nortonsmith",
        "email": "anortonsmith@germantownfriends.org",
    }
)

description = """
As a second-year programming course, this class will explore the real-world applications of software
development. How does Google know what pages to recommend in a search result? How do Instagram filters
change the way photos look? How does a calendar application calculate when repeating events will next
occur? Students will find answers to these questions and more in this project-based class.
"""

print(description.replace("\n", " ").strip())

topics = [
    "Data analysis",
    "Data visualization",
    "Text processing",
    "Numerical simulation",
    "Image processing",
    "Object-oriented programming",
    "Binary and hexadecimal numbers",
]

print("\n".join(f"• {topic}" for topic in topics))

from PIL import Image

im = Image.open("bird.png")
output = Image.new(im.mode, im.size)

for y in range(im.height):
    for x in range(im.width):
        (r, g, b) = im.getpixel((x, y))
        output.putpixel((x, y), (b, r, g))

output.save("output.png")
