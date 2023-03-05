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

    stack = [(root_garums, 1)]
    max_garums = 1
    while stack:
        node, depth = stack.pop()
        max_garums = max(max_garums, depth)
        for child in koks[node]:
            stack.append((child, depth+1))
    
    return max_garums

def main():
    # implement input form keyboard and from files
    ievade = input()
    if "I" in ievade:
         # input number of elements
        n = int(input())
    # input values in one variable, separate with space, split these values in an array
        parents = list(map(int, input().split()))
    if "F" in ievade:
        faila_nosaukums = input()
        path = 'test/'
        # let user input file name to use, don't allow file names with letter a
        if "a" in faila_nosaukums:
            return
        else:
            # Nolasa vērtības no faila
            try:
                with open(path + faila_nosaukums, 'r') as file:
                    n = int(file.readline())
                    parents = list(map(int, file.readline().split()))
            except Exception as ex:
                print("Fails neeksiste", str(ex))
                return

    # account for github input inprecision
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