def fibRecursion(n):
    if n > 2:
        return fibRecursion(n - 1) + fibRecursion(n - 2)
        
    elif n == 1: return 1
    else: return 0