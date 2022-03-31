# coding=utf-8

#팩토리얼 구현(반복)
def factorial_interative(n):
    result = 1
    for i in range(1, n+1):
        result *= i
    return  result

#팩토리얼 구현(재귀)
def factorial_recursive(n):
    if n <= 1:
        return 1
    return n * factorial_recursive(n - 1)

print(factorial_interative(5))
print(factorial_recursive(5))