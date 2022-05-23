# Fibonacci series
# 0, 1, 1, 2, 3, 5, 8...
a = 0
b = 1
for index in range(10):
    print(a)
    old_a = a
    a = b
    b = old_a + b