import sys, time

class Timer:
    def __init__(self, func):
        self.func = func
 
    def __call__(self, *args, **kwargs):
        tic = time.perf_counter_ns()
        self.func(*args, **kwargs)
        toc = time.perf_counter_ns()
        res = (toc - tic)
        return res

def fibRecursion(n):
    if n == 1:
        return 1
    elif n == 0:
        return 0
    return fibRecursion(n - 1) + fibRecursion(n - 2)
    

if __name__== "__main__":
   print(Timer(fibRecursion)(int(sys.argv[1])))
    