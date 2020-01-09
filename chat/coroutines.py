def coroutine(func):
    def inner(*args, **kwargs):
        g = func(*args, **kwargs)
        g.send(None)
        return g

    return inner


def subgen():
    x = 'Ready'
    message = yield x
    print('subgen recieved:', message)


class BlablaException(Exception):
    pass


@coroutine
def average():
    count = 0
    sum = 0
    average = None

    while True:
        try:
            x = yield average
        except StopIteration:
            print('done')
            break
        except BlablaException:
            print('..........')
            break
        else:
            count += 1
            sum += x
            average = round(sum/count, 2)
    return average