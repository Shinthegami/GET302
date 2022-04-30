# This sets the initial condition for x and y and provides storage for y'
plot = {"x": [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0],
        "y": [1.0],
        "y'": []}

iteration = 0
h = .1


def diff_y(X, Y):
    return float(1 - (pow(X, 3)/Y))


def Euler_Y(y0, h, y_0):
    return y0 + h*y_0


for i in range(len(plot["x"])):
    x = plot["x"][i]
    y = plot["y"][i]

    y_ = round(diff_y(x, y), 9)
    plot["y'"].append(y_)

    y1 = round(Euler_Y(y, h, y_), 9)
    plot['y'].append(y1)

print(f" X: ", plot["x"])
print(f" Y: ", plot["y"])
print(f" y': ", plot["y'"])