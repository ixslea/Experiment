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

def harmonicLinean(n):
    sum = 0
    for k in range(1, (n + 1)):
        sum = sum + 1 / k
    return sum
    

if __name__== "__main__":
   print(Timer(harmonicLinean)(int(sys.argv[1])))