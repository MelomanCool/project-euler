from collections import namedtuple
from typing import Iterable

from funcy import rcompose, pairwise, last, takewhile, iterate


def to_digits(number: int) -> Iterable[int]:
    return map(int, str(number))


def is_bouncy(number: int) -> bool:
    pairwise_digits = list(pairwise(to_digits(number)))
    return (not all(a >= b for (a, b) in pairwise_digits)) \
       and (not all(a <= b for (a, b) in pairwise_digits))


State = namedtuple('State', 'i num_of_bouncy proportion_of_bouncy')


def step(prev: State) -> State:
    i = prev.i + 1
    num_of_bouncy = int(is_bouncy(i)) + prev.num_of_bouncy
    return State(
        i,
        num_of_bouncy,
        proportion_of_bouncy = num_of_bouncy / i
    )


if __name__ == '__main__':
    initial_state = State(i = 1, num_of_bouncy = 0, proportion_of_bouncy = 0)
    
    result = rcompose(
        lambda: iterate(step, initial_state),
        lambda xs: takewhile(lambda x: x.proportion_of_bouncy <= 0.99, xs),
        last
    )()
    
    print(result)
