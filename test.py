def Unknown(X, Y):
    if X < Y:
        print(X+Y)
        return Unknown(X + 1, Y) * 2
    else:
        if X == Y:
            return 1
        else:
            print(X+Y)
            return Unknown(X-1, Y) // 2


print(Unknown(10, 15))

