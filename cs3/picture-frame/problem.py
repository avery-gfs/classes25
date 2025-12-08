width = int(input("enter picture width (default 150 mm): ") or 150)
height = int(input("enter picture height (default 100 mm): ") or 100)

back = f"""
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="-1 -1 172 122"
  width="172mm"
  height="122mm"
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

with open("back.svg", "w") as file:
    file.write(back.lstrip())

edges = f"""
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="-1 -1 172 122"
  width="172mm"
  height="122mm"
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

with open("edges.svg", "w") as file:
    file.write(edges.lstrip())

nails = f"""
<svg
  xmlns="http://www.w3.org/2000/svg"
  viewBox="-1 -1 152 29"
  width="152mm"
  height="29mm"
  stroke-width="0.2"
  fill="none"
>
  <rect x="0" y="0" width="150" height="6" stroke="black" />
  <rect x="0" y="7" width="150" height="6" stroke="black" />
  <rect x="0" y="14" width="100" height="6" stroke="black" />
  <rect x="0" y="21" width="100" height="6" stroke="black" />
</svg>
"""

with open("nails.svg", "w") as file:
    file.write(nails.lstrip())
