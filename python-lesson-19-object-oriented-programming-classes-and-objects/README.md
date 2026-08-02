# Python Classes & Objects — Lesson 19

## Problem

Tracking multiple related things (dogs, users, cars) with separate loose
variables (`dog1_name`, `dog1_age`, `dog2_name`, `dog2_age`, ...) doesn't
scale. Nothing in the code enforces the relationship between a variable pair
— it's a naming convention maintained by memory, and it breaks down past a
handful of entities.

## Intuition

When you notice data that belongs together (a name + age describing one
dog) and behavior tied to that data (a dog can bark), that's the signal to
stop using loose variables and define a class: a blueprint describing what
every object of that type has and does.

## Approach

- Define the blueprint once with `class Dog:`
- Use `__init__` to set up each object's required starting state the
  moment it's created
- Use `self` inside methods to refer to "the object this method is
  currently running on" — this is what keeps each object's data independent
- Create as many objects as needed from the same class; each holds its own
  copy of the data

## Python Solution

\`\`\`python
class Dog:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def bark(self):
        print(f"{self.name} says woof!")


rex = Dog("Rex", 3)
milo = Dog("Milo", 5)

rex.bark()   # Rex says woof!
milo.bark()  # Milo says woof!
\`\`\`

## Complexity

- **Time:** O(1) to create an object or call a method
- **Space:** O(n) for n objects, each with its own independent attribute
  storage

## Video

Full walkthrough: (video link coming soon)

## Article

Full written lesson with dry run, common mistakes, and interview questions:
(video link coming soon)
