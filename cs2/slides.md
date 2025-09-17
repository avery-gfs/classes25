## PIL Library

Starter code

```py
from PIL import Image

# Load input image
im = Image.open("bird.png")

# Make blank output image with same dimension as the original
output = Image.new(im.mode, (im.width, im.height))

for y in range(im.height):
  for x in range(im.width):
    (r, g, b) = im.getpixel((x, y))

    # Your code goes here
    
    output.putpixel((x, y), (r, g, b))

# Save output image
output.save("grayscale.png")
```

<aside class="notes">
  Shhh, these are your private notes 📝
</aside>

---

## Grayscale

<img width="450" src="/images/bird.png" />

<img width="450" src="/images/grayscale/grayscale.png" />

---

## Greenish

<img width="450" src="/images/bird.png" />

<img width="450" src="/images/greenish/greenish.png" />

---

## Fancy grayscale

Relative / perceptual luminance

$$l = 0.2126 \cdot r + 0.7152 \cdot g + 0.0722 \cdot b$$

https://en.wikipedia.org/wiki/Relative_luminance

<img width="450" src="/images/grayscale/grayscale.png" />

<img width="450" src="/images/fancy-grayscale/fancy-grayscale.png" />

---

## Inverted

$$r = 255 - r$$
$$g = 255 - g$$
$$b = 255 - b$$

<img width="450" src="/images/bird.png" />

<img width="450" src="/images/inverted/inverted.png" />

---

**PIL intro**

- https://pillow.readthedocs.io/en/stable/reference/Image.html

- Dimensions

  ```py
  im.height # image height in pixels
  im.width # image width in pixels
  ```

- Get pixel value:

  ```py
  (r, g, b) = im.getpixel((x, y)) # get rgb values at position x, y
  ```

- Set pixel value:

  ```py
  im.putpixel((x, y), (r, g, b)) # set rgb values at position x, y
  ```

**Starter code**

**Demo manipulation**

Set `r = 255`.

**Grayscale**

- *Problem*

**Greenish**

- *Problem*
