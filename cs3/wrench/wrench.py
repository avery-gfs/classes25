import os

width = int(input("enter socket width (mm) (10): ") or 10)

wrench = f"""
<svg
  width="400mm"
  height="200mm"
  viewBox="0 0 400 200"
  stroke="black"
  fill="none"
  xmlns="http://www.w3.org/2000/svg"
>

  <g
    transform="translate(100 100) scale({width / 10})"
    stroke-width="{4 / width}"
  >
    <path
      d="
        M -2.89 -5
        h 5.77
        l 2.89 5
        l -2.89 5
        h -5.77
        l -2.89 -5
        z
      "
    />

    <path
      d="
        M 0 -12
        h 80
        v 24
        h -80
        a 10 10 0 0 1 0 -24
      "
    />

    <text
      x="40"
      y="1"
      text-anchor="middle"
      dominant-baseline="middle"
      style="font-size: 10px; font-family: monospace"
    >
      {width} mm
    </text>
  </g>
</svg>
"""

with open(f"{width}mm.svg", "w") as file:
    file.write(wrench.lstrip())
