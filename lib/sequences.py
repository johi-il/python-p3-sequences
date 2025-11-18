#!/usr/bin/env python3

def print_fibonacci(length):
    if length <= 0:
        print([])
        return 
    fib_list = []
    a, b = 0, 1
    for i in range(length):
        fib_list.append(a)
        a, b = b, a + b
    print(fib_list)
