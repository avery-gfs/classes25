width = int(input("enter picture width (default 150 mm): ") or 150)
height = int(input("enter picture height (default 100 mm): ") or 100)

back = f"""
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="-1 -1 {width + 22} {height + 22}"
  width="{width + 22}mm"
  height="{height + 22}mm"
  stroke-width="0.2"
  fill="none"
>
  <rect x="0" y="0" width="{width + 20}" height="{height + 20}" stroke="black" />

  <rect x="10" y="3.5" width="{width}" height="3" stroke="red" />
  <rect x="10" y="{height + 13.5}" width="{width}" height="3" stroke="red" />
  <rect x="3.5" y="10" width="3" height="{height}" stroke="red" />
  <rect x="{width + 13.5}" y="10" width="3" height="{height}" stroke="red" />

  <rect x="{width / 2}" y="12" width="20" height="3" stroke="red" />
  <rect x="12" y="{height / 2}" width="3" height="20" stroke="red" />
</svg>
"""

with open("back.svg", "w") as file:
    file.write(back.lstrip())

edges = f"""
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="-1 -1 {width + 22} {height + 22}"
  width="{width + 22}mm"
  height="{height + 22}mm"
  stroke-width="0.2"
  fill="none"
>
  <path d="m 0 0 h {width + 20} l -10 10 h -{width} z" stroke="black" />
  <path d="m 0 {height + 20} h {width + 20} l -10 -10 h -{width} z" stroke="black" />
  <path d="m 0 0 v {height + 20} l 10 -10 v -{height} z" stroke="black" />
  <path d="m {width + 20} 0 v {height + 20} l -10 -10 v -{height} z" stroke="black" />

  <rect x="10" y="3.5" width="{width}" height="3" stroke="red" />
  <rect x="10" y="{height + 13.5}" width="{width}" height="3" stroke="red" />
  <rect x="3.5" y="10" width="3" height="{height}" stroke="red" />
  <rect x="{width + 13.5}" y="10" width="3" height="{height}" stroke="red" />
</svg>
"""

with open("edges.svg", "w") as file:
    file.write(edges.lstrip())

nails = f"""
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="-1 -1 {max(width, height) + 2} 30.5"
  width="{max(width, height) + 2}mm"
  height="29mm"
  stroke-width="0.2"
  fill="none"
>
  <rect x="0" y="0" width="{width}" height="6.4" stroke="black" />
  <rect x="0" y="7.5" width="{width}" height="6.4" stroke="black" />
  <rect x="0" y="15" width="{height}" height="6.4" stroke="black" />
  <rect x="0" y="22.5" width="{height}" height="6.4" stroke="black" />
</svg>
"""

with open("nails.svg", "w") as file:
    file.write(nails.lstrip())
