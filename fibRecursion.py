import sys

def fibRecursion(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fibRecursion(n - 1) + fibRecursion(n - 2)
    

if __name__== "__main__":
   print(fibRecursion(int(sys.argv[1])))
    