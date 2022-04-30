plot = {"x": [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1],
        "y": [1.0],
        "y'": [],
        "aux_y": [0]}

iteration = 0
h = .1


def y_x(X, Y):
    return round(float(1 - (pow(X, 3)/Y)), 9)


for i in range(len(plot["x"]) -2):
    x = plot["x"][i]
    y = plot["y"][i]

    if i == 0:
        dy_dx = y_x(x, y)
        plot["y'"].append(dy_dx)

    aux_y = y + h*dy_dx
    plot["aux_y"].append(aux_y)

    xi = plot["x"][i+1]
    yi = round(y + 0.5 * h * (dy_dx + y_x(xi, aux_y)), 9)

    plot["y"].append(yi)
    dy_dx = y_x(xi, yi)
    plot["y'"].append(dy_dx)

print(f" X: ", plot["x"])
print(f" Y: ", plot["y"])
print(f" y': ", plot["y'"])
print(f" aux_y: ", plot["aux_y"])
