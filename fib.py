# 0 1 1 2 3 5 8 13 21
def fib_function(n):
    if (n < 2):
        return n
    x = 0
    y = 1
    i = 2

    while i <= n:
        y = y + x
        x = y - x
        i = i + 1
    return y

a = 0
while a <= 10:
    print(f"Dla n równego: {a} ciąg fibbonaciego jest równy: {fib_function(a)}")
    a = a + 1
