from typing import Union, Iterable, Any, Optional


def assert_types(
        type_: Union[type, tuple[type]],
        li: Iterable[Any],
        msg:Optional[str]=None):
    for x in li:
        if not isinstance(x, type_):
            if msg is None:
                msg = "assert_types failed"
            msg += f" excpected all elements to be {type_}" \
                   f" but {x} was found (type: {type(x)})"
            raise TypeError(msg)
