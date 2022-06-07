# 중복순열 라이브러리
from itertools import product

n = 4
print(list(product([ '+', '-', '*', '/'], repeat=(n - 1))))