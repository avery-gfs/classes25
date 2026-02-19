import os

width = int(input("enter picture width (mm) (default 150): ") or 150)
height = int(input("enter picture height (mm) (default 100): ") or 100)

directory = f"{width}-by-{height}"
os.makedirs(directory, exist_ok=True)

nails = f"""
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 400 400"
  width="400mm"
  height="400mm"
  stroke-width="0.2"
  fill="none"
>
  <rect x="0" y="0" width="{width}" height="6.2" stroke="black" />
  <rect x="0" y="7.5" width="{width}" height="6.2" stroke="black" />
  <rect x="0" y="15" width="{height}" height="6.2" stroke="black" />
  <rect x="0" y="22.5" width="{height}" height="6.2" stroke="black" />
</svg>
"""

with open(f"{directory}/nails.svg", "w") as file:
    file.write(nails.lstrip())

back = f"""
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 400 400"
  width="400mm"
  height="400mm"
  stroke-width="0.2"
  fill="none"
>
  <rect x="0" y="0" width="170" height="120" stroke="black" />

  <rect x="10" y="3.5" width="150" height="3" stroke="red" />
  <rect x="10" y="113.5" width="150" height="3" stroke="red" />
  <rect x="3.5" y="10" width="3" height="100" stroke="red" />
  <rect x="163.5" y="10" width="3" height="100" stroke="red" />

  <rect x="75.0" y="12" width="20" height="3" stroke="red" />
  <rect x="12" y="50.0" width="3" height="20" stroke="red" />
</svg>
"""

with open(f"{directory}/back.svg", "w") as file:
    file.write(back.lstrip())

edges = f"""
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 400 400"
  width="400mm"
  height="400mm"
  stroke-width="0.2"
  fill="none"
>
  <path d="m 0 0 h 170 l -10 10 h -150 z" stroke="black" />
  <path d="m 0 120 h 170 l -10 -10 h -150 z" stroke="black" />
  <path d="m 0 0 v 120 l 10 -10 v -100 z" stroke="black" />
  <path d="m 170 0 v 120 l -10 -10 v -100 z" stroke="black" />

  <rect x="10" y="3.5" width="150" height="3" stroke="red" />
  <rect x="10" y="113.5" width="150" height="3" stroke="red" />
  <rect x="3.5" y="10" width="3" height="100" stroke="red" />
  <rect x="163.5" y="10" width="3" height="100" stroke="red" />
</svg>
"""

with open(f"{directory}/edges.svg", "w") as file:
    file.write(edges.lstrip())

stand = f"""
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="0 0 400 400"
  width="400mm"
  height="400mm"
  stroke-width="0.2"
  fill="none"
>
  <path d="m 0 0 h 45 v 4 h 3.2 v 20 h -3.2 v 4 h -45 z" stroke="black" />
</svg>
"""

with open(f"{directory}/stand.svg", "w") as file:
    file.write(stand.lstrip())
