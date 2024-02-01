def fibonacci_like_sum(limit):
    a, b = 3, 4
    total_sum = 0

    while a <= limit:
        if a % 2 == 0:
            total_sum += a
        a, b = b, a + b

    return total_sum

limit = 7000000
result = fibonacci_like_sum(limit)
print(f"The sum of even-valued terms not exceeding {limit} is: {result}")
