def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b

nums = fibonacci()
for i in range(8):
    print(next(nums))