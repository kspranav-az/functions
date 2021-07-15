
def si(principal, year, rate):                # all  positional arguments
    simple = (principal * rate * year) / 100
    return simple


def si1(principal, year, rate=1):           # rate and year are a default argument
    simple = (principal * rate * year) / 100
    return simple


sim = si1(principal=1000, rate=12, year=2)  # all keyword or named arguments

sim1 = si1(1000, rate=12, year=2) # using keyword argument with positional

# sim2 = si1(principal=1000,12,2) #illegal


