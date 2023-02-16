def f(pow):
    def g(*args):
        print("ARGS:")
        print(args)
        return pow(*reversed(args))
    return g


print(pow(2, 3))

reverse_pow = f(pow)
print(reverse_pow(3, 2))

