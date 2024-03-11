from typing import TypeVar

T = TypeVar('T')


def mutate_tuple(tpl: tuple[T, ...], index: int, new_value: T) -> tuple[T, ...]:
    return tpl[:index] + (new_value, ) + tpl[(index+1):]
