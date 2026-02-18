import math


def generate_lowpass_points(N=200, alpha=0.1):
    x_vals = []
    y_vals = []

    # generate input signal (low + high frequency)
    for n in range(N):
        x = math.sin(0.05 * n) + 0.5 * math.sin(0.5 * n)
        x_vals.append(x)

    # apply filter
    y_prev = x_vals[0]
    for n in range(N):
        y = alpha * x_vals[n] + (1 - alpha) * y_prev
        y_vals.append(y)
        y_prev = y

    return x_vals, y_vals


# ---- RUN ----
N = 200
alpha = 0.9

x, y = generate_lowpass_points(N, alpha)
output = "["

for n in range(N):
    output += f"({n}, {y[n]}), "

output += "]"
print(output)

import math


def generate_highpass_points(N=200, alpha=0.9):
    x_vals = []
    y_vals = []

    # generate input signal
    for n in range(N):
        x = math.sin(0.05 * n) + 0.5 * math.sin(0.5 * n)
        x_vals.append(x)

    # apply filter
    y_prev = 0
    x_prev = x_vals[0]

    for n in range(N):
        y = alpha * (y_prev + x_vals[n] - x_prev)
        y_vals.append(y)

        y_prev = y
        x_prev = x_vals[n]

    return x_vals, y_vals


# ---- RUN ----
N = 200
alpha = 0.9

x, y = generate_highpass_points(N, alpha)
output = "["

for n in range(N):
    output += f"({n}, {y[n]}), "

output += "]"
print(output)
