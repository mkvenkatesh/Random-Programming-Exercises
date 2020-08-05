# A closure is a function where every free variable, everything except
# parameters, used in that function is bound to a specific value defined in the
# enclosing scope of that function. In effect, closures define the environment
# in which they run, and so can be called from anywhere.

def outer_func(x):
    y = 4
    def inner_func(z):
        print(f"x = {x}, y = {y}, z = {z}")
        return x + y + z

    return inner_func

for i in range(3):
    closure = outer_func(i)
    print(f"closure({i+5}) = {closure(i+5)}")
