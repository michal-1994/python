def fibonacci_function(n: int) -> int:
    """Calculates the nth Fibonacci number using an iterative approach.

    Args:
        int (n): The index of the desired Fibonacci number

    Returns:
        int: The nth Fibonacci number

    """
    if (n < 2):
        return n

    x, y = 0, 1

    for _ in range(2, n + 1):
        x, y = y, x + y

    return y

def print_fibonacci_sequence(limit: int) -> None:
    """Prints the Fibonacci sequence up to a specified limit.

    Args:
        string (limit): The upper limit for printing the Fibonacci sequence

    """
    for i in range(limit + 1):
        print(f"For n = {i}, the Fibonacci number is: {fibonacci_function(i)}")

# Result: 0 1 1 2 3 5 8 13 21 34 55
print_fibonacci_sequence(10)
