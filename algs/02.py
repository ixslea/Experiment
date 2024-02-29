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

def fibIterative(n):
    a = 0
    b = 1
    for _ in range(n):
        a, b = b, a + b
    return a
    

if __name__== "__main__":
   print(Timer(fibIterative)(int(sys.argv[1])))
