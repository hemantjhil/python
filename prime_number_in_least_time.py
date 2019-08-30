{
#Initial Template for Python 3
//Position this line where user code will be pasted.
import math ##You will need this for prime checking
    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        number=int(input())
        print(isPrime(number)) ##This isPrime is function that you need to create
        testcases-=1
        
if __name__=='__main__':
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
##Write the function completely
def isPrime(number):
    b=True;
    for i in range(2,int(math.sqrt(number))):
        if(number%i==0):
            b=False
            break;
    return b
