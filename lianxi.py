# def my_abs(x):
#     if x >= 0:
#         return x
#     else:
#         return -x


# def power(x,n):
#     s = 1
#     while n>0:
#         n = n-1
#         s = s * x
#     return s
# print(power(5,3))


# def fact(n):
#     if n==1:
#         return 1
#     return n * fact(n - 1)
# print(fact(1000))

def fact(n):
    return fact_iter(n, 1)

def fact_iter(num, product):
    if num == 1:
        return product
    return fact_iter(num - 1, num * product)

print(fact(10))