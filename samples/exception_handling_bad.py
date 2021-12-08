import time


def do_something():
    raise ValueError("Something bad happened...")


# Don't do this
try:
    do_something()
except:
    pass


def do_something():
    print("I can't die!")
    time.sleep(1.0)
    raise SystemExit(0)


# Really don't do this
while True:
    try:
        do_something()
    except BaseException:
        pass
