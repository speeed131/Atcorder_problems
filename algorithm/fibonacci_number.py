def fibonacci(count):
    
    if (count == 1) or (count == 2):
        return 1
    return fibonacci(count - 2) + fibonacci(count - 1)

print([fibonacci(i) for i in range(1, 10)])
