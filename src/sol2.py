from itertools import takewhile

def fibonacci():
    a, b = 1, 1
    while True:
        yield a
        a, b = b, a+b


def febbb():
    a, b = 1, 1
    while a < 4_000_000:
        yield a
        a, b = b, a+b


def even(it):
    for n in it:
        if n % 2 == 0:
            yield n


if __name__ == "__main__":
    # getEvenSum()
    # print(sum(takewhile(lambda f: f <= 4000000, even(fibonacci()))))
    print(sum(even(febbb())))