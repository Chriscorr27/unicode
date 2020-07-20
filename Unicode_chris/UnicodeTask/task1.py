

def task(a,b):
    res = {}
    for j in range(a,b):
        B = format(j,'0b')
        #print(len(b))
    
        ans = False
        for i in range(len(B)-1):
            if(B[i]=='1' and B[i+1]=='1'):
                ans = True
                break
        res[j]=ans
    return res