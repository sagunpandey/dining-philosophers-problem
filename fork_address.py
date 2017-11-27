def get_number_of_forks():
    return len(forks)


def get_fork(index):
    return forks[index]


def get_fork_left(index):
    fork = get_fork(index % get_number_of_forks())
    if fork:
        return fork
    else:
        return get_fork(len(forks) - 1)


def get_fork_right(index):
    fork = get_fork((index + 1) % get_number_of_forks())
    if fork:
        return fork
    else:
        return get_fork(len(forks) - 1)


forks = [['localhost', 4000],
         ['localhost', 4001],
         ['localhost', 4002],
         ['localhost', 4003],
         ['localhost', 4004]]
