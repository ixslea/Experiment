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

def harmonicRecursion(n):
    if n <= 2:
        return 1
    else:
        return harmonicRecursion(n - 1) + (1 / n)
    

if __name__== "__main__":
   print(Timer(harmonicRecursion)(int(sys.argv[1])))