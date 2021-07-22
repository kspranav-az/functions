# non void function
def add(x, y):
    ad = x + y
    return ad


count = add(2, 3)

print(count)


# void function
def sub(x, y):
    ad = x - y
    print(ad)


sub(3, 2)

''' TYPE OF VALUES RETURNED IN NON VOID FUNCTIONS '''


# literals

def retfive():
    return 5


def retstr():
    return "alphabets"


print(retfive(), retstr())

# variable

""""
def add(x, y):
    ad = x + y
    return ad
"""


def addstr(a, b):
    s = a + b
    return str(s)


print(add(2, 1), addstr("bom", "bom"))


# expressions

def add1(a, b):
    return a + b


def wtf(a, b, c):
    return (a ** 2 + b * 5 + c) / c ** 2 * b


print(add1(10, 12), wtf(3, 4, 5))

''' TYPE OF VALUE RETURNED IN VOID FUNCTION '''


# IF RETURN NOT USED RETURNS NONE

def quote():  # void function
    print("think positive.")


print(quote())


# IF RETURN IS ALSO USED THEN EXECUTE THE FUNCTION AND RETURNS THE VALUE ALSO

def quote1(reply="I got it."):
    print("think positive")
    return reply


print(quote1())

''' RETURNING MULTIPLE VALUES '''


def retmulti(a, b):
    return a + b, a - b, a * b


a, b, c = retmulti(2, 1)

print(retmulti(2, 1), a, b, c)
