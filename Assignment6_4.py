import threading
from functools import reduce

def find_sum(lst):
    print("Sum =", sum(lst))

def find_product(lst):
    product = reduce(lambda x, y: x * y, lst)
    print("Product =", product)

lst = list(map(int, input("Enter numbers separated by space: ").split()))

t1 = threading.Thread(target=find_sum, args=(lst,))
t2 = threading.Thread(target=find_product, args=(lst,))

t1.start()
t2.start()

t1.join()
t2.join()
