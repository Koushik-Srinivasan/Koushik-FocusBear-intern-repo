# This is bad, commented code (example for issue #46)

def calc(a, b, c):
    # add a and b
    x = a + b
    # multiply x by c
    y = x * c
    # set discount to 0.1
    discount = 0.1
    # if y is greater than 100
    if y > 100:
        # subtract discount from y
        y = y - (y * discount)
    # return y
    return y
