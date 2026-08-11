from typing import TypeVar, List

T = TypeVar("T")

def first(items: List[T]) -> T:
    return items[0]

first([1, 2, 3])       # int in, int out
first(["a", "b"])       # str in, str out
