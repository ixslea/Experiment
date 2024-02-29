import matplotlib.pyplot as plt, sys

def plotting(steps, results, algName):

    x = [i for i in range(1, steps+1)]

    plt.plot(x, results, '-o', color = "blue", label = f"{algName}: average execution time (ns)")
    plt.legend()
    plt.savefig(f'resultPlots/{algName}_average.png')
    plt.close()

    plt.plot(x, results, '-o', color = "blue", label = f"{algName}: average execution time (ns) (log-scale plot)")
    plt.legend()
    plt.yscale('log')
    plt.savefig(f'resultPlots/{algName}_average_log_scaled.png')
    plt.close()

if __name__== "__main__":
   plotting(int(sys.argv[1]), int(sys.argv[2]), int(sys.argv(3)))