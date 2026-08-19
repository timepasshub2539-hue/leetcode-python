# Python Object Model: Descriptors, `__slots__`, MRO, and Metaclasses

A minimal, working demonstration of how `obj.attr` actually resolves in Python,
and the four mechanisms that can intercept or shape that resolution.

## Problem

Two near-identical classes behave differently when you try to add a new
attribute to an instance after construction: one accepts it, one raises
`AttributeError`. This repo demonstrates why, and builds out the related
concepts (descriptors, MRO, metaclasses) that explain the rest of Python's
attribute and class-construction protocol.

## Intuition

`obj.attr` is a search across the type and the instance, not a direct
dictionary grab. Descriptors are class attributes that implement `__get__`
and `__set__` and get to intercept that search. `__slots__` removes the
per-instance `__dict__` that flexible attribute assignment depends on. MRO
determines method resolution order deterministically when there's ambiguity
across parent classes. Metaclasses control how a class itself is built.

## Approach

1. Build a data descriptor (`NonNegative`) that validates on every write.
2. Attach it to a class (`Account`) so all assignments route through it.
3. Demonstrate `__slots__` removing per-instance flexibility.
4. Inspect `ClassName.__mro__` to resolve multiple-inheritance ambiguity.
5. Write a metaclass that auto-registers every subclass on definition.

## Python Solution

```python
class NonNegative:
    def __set_name__(self, owner, name):
        self._name = "_" + name

    def __get__(self, instance, owner):
        if instance is None:
            return self
        return getattr(instance, self._name)

    def __set__(self, instance, value):
        if value < 0:
            raise ValueError(f"{self._name.lstrip('_')} cannot be negative")
        setattr(instance, self._name, value)


class Account:
    balance = NonNegative()

    def __init__(self, balance):
        self.balance = balance


class Meta(type):
    registry = {}

    def __new__(mcs, name, bases, namespace):
        cls = super().__new__(mcs, name, bases, namespace)
        mcs.registry[name] = cls
        return cls


class Plugin(metaclass=Meta):
    pass


class CsvPlugin(Plugin):
    pass


assert "CsvPlugin" in Meta.registry
```

## Complexity

- Descriptor read/write: O(1) time, O(1) additional space per instance.
- MRO computation: happens once at class-definition time (C3 linearization),
  not on every attribute access.

## Video

Full walkthrough with a live demo of the two-class puzzle: (video link coming soon)

## Article

Complete written breakdown with dry runs, edge cases, and interview
questions: see the linked article.
