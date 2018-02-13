def fibo(n):
    if(n<=1):
        return 1
    return fibo(n-1)+fibo(n-2)

def producto (n1, n2):
    if(n2!=0 and n1!=0): return producto(n1,n2-1)
    if(n2==1): return n1
    
    else: return n1+n1
    
    
    
        
    
