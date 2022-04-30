plot = {"x": [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        "y": [1]}

iteration = 0
h = .1


def y_x(X, Y):
    return round(float(1 - (pow(X, 3)/Y)), 5)


x0 = plot["x"][0]
y0 = plot["y"][0]

k1 = h * y_x(x0, y0)
k2 = h * y_x(x0 + 0.5 * h, y0 + 0.5 * k1)
k3 = h * y_x(x0 + 0.5 * h, y0 + 0.5 * k2)
k4 = h * y_x(x0 + h, y0 + k3)

diff_y = (1/6) * (k1 + 2 * k2 + 2 * k3 + k4)

for i in range(len(plot["x"]) - 1):
    y = plot["y"][i]
    y1 = y + diff_y
    y1 = round(y1, 9)
    plot["y"].append(y1)

print(f" X: ", plot["x"])
print(f" Y: ", plot["y"])