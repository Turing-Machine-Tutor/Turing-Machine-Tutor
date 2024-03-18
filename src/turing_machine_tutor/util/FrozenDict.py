from typing import TypeVar, Generic, Mapping, Iterator, ValuesView, AbstractSet, Tuple, Optional, overload, \
    Union

_K = TypeVar('_K')
_V = TypeVar('_V')
_T = TypeVar('_T')

class FrozenDict(Generic[_K, _V], Mapping[_K, _V]):
    def __init__(self, *args, **kwargs):
        if not args:
            self._dict: dict[_K, _V] = {**kwargs}
        elif len(args) != 1:
            raise Exception("if not using kwargs, should have one argument and it should be of type Mapping")
        else:
            try:
                self._dict = {**(args[0])}
            except:
                raise Exception("if not using kwargs, should have one argument and it should be of type Mapping")

    def __getitem__(self, k: _K) -> _V:
        return self._dict[k]

    def __len__(self) -> int:
        return len(self._dict)

    def __iter__(self) -> Iterator[_K]:
        return iter(self._dict)

    def __repr__(self):
        return f'frozendict({repr(self._dict)})'

    def __str__(self):
        return f'frozendict({str(self._dict)})'

    @overload
    def get(self, key: _K) -> Optional[_V]:
        return self._dict.get(key)

    @overload
    def get(self, key: _K, default: Union[_V, _T]) -> Union[_V, _T]:
        return self._dict.get(key, default)

    def items(self) -> AbstractSet[Tuple[_K, _V]]:
        return self._dict.items()

    def keys(self) -> AbstractSet[_K]:
        return self._dict.keys()

    def values(self) -> ValuesView[_V]:
        return self._dict.values()

    def __contains__(self, o: object) -> bool:
        return o in self._dict

    def _as_immutable(self):
        return frozenset(self._dict.items())

    def __eq__(self, other):
        if isinstance(other, FrozenDict):
            return self._dict == other._dict
        if isinstance(other, dict):
            return self._dict == other
        if isinstance(other, Mapping):
            return self._dict == {**other}
        else:
            raise TypeError(other)
