import numpy as np

def isprime(x):
    y=np.ceil(np.sqrt(x))+1
    if x==2:
        return True
    if x==1:
        return False
    for t in range (2,int(y)):
        if (x%t) ==0:
            return False
            break
    else:
        return True