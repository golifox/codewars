"""Create a function that takes an integer as an argument and returns "Even" 
for even numbers or "Odd" for odd numbers."""


def even_or_odd(number: int) -> str:
    return "Even" if not number % 2 else "Odd"
