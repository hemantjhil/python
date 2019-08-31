#code
import numpy as np
def main():
    t=int(input())
    while(t>0):
        m,n=[int(x) for x in input().split()]
        #a=[]
        e=list(map(int,input().split()))
        a=np.array(e).reshape(m,n)
        k=0;l=0
        while(k<m and l<n):
            for i in range(l,n):
                print(a[k][i],end=" ")
                
            k+=1;
            for i in range(k,m):
                print(a[i][n-1],end=" ")
                
            n-=1
            if(k<m):
                for i in range(n-1,l-1,-1):
                    print(a[m-1][i],end=" ")
                
                m-=1;
            if(l<n):
                for i in range(m-1,k-1,-1):
                    print(a[i][l],end=" ")
                
                l+=1
        
        t-=1;
        print()
if __name__=='__main__':
    main()
