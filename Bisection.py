roots = [-1, -3]    # Sets the range of values for the roots
approx_root = []    # To store the approximations of the roots
iteration = 0       # Increment counter to keep track of the iteration


# This is the problem function
def f(x):
    return pow(x, 3) + 3 * pow(x, 2) + 5*x + 9


x_0 = (roots[1] + roots[0])/2
approx_root.append(x_0)

while True:
    if f(x_0) > 0:
        roots[0] = x_0
    elif f(x_0) < 0:
        roots[1] = x_0
    else:
        print(f"Root = {f(x_0)}")
        break

    iteration += 1
    x_0 = (roots[1] + roots[0])/2
    approx_root.append(x_0)
    # print(f"Iteration{iteration}: {approx_root[iteration]}")

    if abs(approx_root[iteration] - approx_root[iteration-1]) < 0.00001:
        # print(f"Root = {round(approx_root[iteration], 4)}")
        break


print(f"Roots: {approx_root}")