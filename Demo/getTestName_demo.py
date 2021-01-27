import inspect


def whoami():
    return inspect.stack()[1][3]

def myFunc():
    x = whoami()
    print(x)


myFunc()