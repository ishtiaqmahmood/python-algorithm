from tqdm import *

import progressbar 



def fibonacci(n):
    widgets = ['Loading: ', progressbar.AnimatedMarker()] 
    bar = progressbar.ProgressBar(widgets=widgets).start()
    assert n >= 0 and int(n) == n, 'Fibonacci number cannot be negative number or non integer'
    if n in [0,1]:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    bar.update(n)

    
userInput = int(input('Enter Positive Integer: '))
print(fibonacci(userInput))
