approx_root = []    # Stores the approximate roots for each iteration
fx = []             # Stores the result of the function for each value of the root
f_x = []            # Stores the result of the first derivative for each value of the root
iteration = 0       # Increment counter to keep track of the iteration


# This is the problem function
def f(x):
    return pow(x, 3) + 3 * pow(x, 2) + 5*x + 9


# This is the derivative of the function
def f_(x):
    return 3 * pow(x, 2) + 6 * x + 5


# Sets the initial conditions for all of the variables
x_0 = -2
approx_root.append(x_0)
fx.append(f(x_0))
f_x.append(f_(x_0))

while True:
    iteration += 1

    x_ = approx_root[iteration-1]
    x = x_ - (f(x_)/f_(x_))
    approx_root.append(x)
    fx.append(f(x))
    f_x.append(f_(x))
    # print(f"Iteration {iteration} : {x}")

    # if abs(x - x_) < pow(10, -4):
    #     break
    if iteration > 14:
        break

for i in range(iteration):
    print(f"Iteration: {i}  x: {round(approx_root[i], 4)}   f(x): {round(fx[i], 4)} f'(x): {round(f_x[i], 4)}")