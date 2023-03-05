# python3

import sys
import threading
import numpy


def compute_height(n, parents):
    koks = [[] for i in range(n)]
    for i in range(n):
        parent_garums = parents[i]
        if parent_garums == -1:
            root_garums = i
        else:
            koks[parent_garums].append(i)

    def atrast(node):
        if not koks[node]:
            return 1
        garums = [atrast(child) for child in koks[node]]
        return 1 + max(garums)
    return atrast(root_garums)

def main():
    # implement input form keyboard and from files
    ievade = input()
    if "I" in ievade:
         # input number of elements
        n = int(input())
        parents = list (map(int, input().split () ))
    if "F" in ievade:
        mape = './test/'
        while True:
            faila_nosaukums = input()
            if "a" in faila_nosaukums:
                print("Faila nosaukumā nevar būt burts 'a' ")
            else:
                break
        vieta = mape + faila_nosaukums
        with open(vieta, 'r') as f:
            n = int(f.readline().strip())
            parents = list(map(int, f.readline().strip().split()))
    # let user input file name to use, don't allow file names with letter a
    # account for github input inprecision

    # input values in one variable, separate with space, split these values in an array
    # call the function and output it's result
    result = compute_height(n, parents)
    print(result)

# In Python, the default limit on recursion depth is rather low,
# so raise it here for this problem. Note that to take advantage
# of bigger stack, we have to launch the computation in a new thread.
sys.setrecursionlimit(10**7)  # max depth of recursion
threading.stack_size(2**27)   # new thread will get stack of such size
threading.Thread(target=main).start()
main()
# print(numpy.array([1,2,3]))