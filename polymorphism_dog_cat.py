
"""
Demonstrate polymorphism using method overriding
with Animal, Dog, and Cat classes.
"""


class Animal:
    """Base class representing an animal."""

    def speak(self):
        """Return a generic animal sound."""
        return "Animal makes a sound."


class Dog(Animal):
    """Dog subclass inheriting from Animal."""

    def speak(self):
        """Override speak() to return a dog sound."""
        return "Woof!"


class Cat(Animal):
    """Cat subclass inheriting from Animal."""

    def speak(self):
        """Override speak() to return a cat sound."""
        return "Meow!"


def main():
    """Create animal objects and demonstrate polymorphism."""
    dog = Dog()
    cat = Cat()

    print(f"Dog says: {dog.speak()}")
    print(f"Cat says: {cat.speak()}")


if __name__ == "__main__":
    main()