def avg(marks):
    Te = len(marks)
    s = sum(marks)
    avg = s / Te
    return avg


def si(principal, year, rate):
    simple = (principal * rate * year) / 100
    return simple


print(si(1000, 2, 12))
