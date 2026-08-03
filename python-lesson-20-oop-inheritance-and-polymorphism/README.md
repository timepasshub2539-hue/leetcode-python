# Python Inheritance: Fix the Bug That Waits Until Your 5th Class

## Problem

You have several classes that represent variations of the same concept
(Dog, Cat, Bird, ...). Each needs shared setup (like storing a `name`) and
its own unique behavior (like `make_sound`). Writing each class independently
means duplicating the shared logic across every one — and any future change
to that shared logic has to be repeated everywhere it was copied.

## Intuition

Duplicated `__init__` logic across similar classes is a signal that a shared
concept is hiding underneath them. Pull that shared part into one parent
class. Let each specific class inherit it instead of rewriting it, and
override only the methods that genuinely need to differ.

## Approach

1. Create a parent class (`Animal`) holding shared setup.
2. Subclass it (`class Dog(Animal):`) so child classes inherit that setup
   automatically.
3. Override `make_sound()` in each subclass where behavior differs.
4. Use `super().__init__()` when a subclass needs extra setup, so it extends
   the parent instead of duplicating it.
5. Recognize when inheritance isn't needed at all — if you only need shared
   *behavior*, not shared *state*, duck typing (any object with the right
   method) is simpler.

## Python Solution

\`\`\`python
class Animal:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} makes a sound."


class Dog(Animal):
    def __init__(self, name, breed=None):
        super().__init__(name)
        self.breed = breed

    def make_sound(self):
        return f"{self.name} says Woof!"


class Cat(Animal):
    def make_sound(self):
        return f"{self.name} says Meow!"


class Bird(Animal):
    def make_sound(self):
        return f"{self.name} says Tweet!"


class Person:
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        return f"{self.name} says Quack! (I'm just pretending)"


def make_it_sound(thing):
    return thing.make_sound()
\`\`\`

## Complexity

- **Time:** O(1) per method call — Python resolves methods via a class
  lookup chain, not a linear scan.
- **Space:** O(1) additional space per object — the parent's code is shared
  once across all subclasses, never duplicated per instance.

## Video

Full walkthrough with the class family tree diagram: (video link coming soon)

## Article

Full written breakdown, dry run, edge cases, and interview questions: see
the accompanying article in this repo / linked in the video description.
