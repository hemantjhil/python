{
#Initial Template for Python 3
//Position this line where user code will be pasted.    
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        base=int(input())
        exp=int(input())
        print(power(base,exp)) ##calling the anonymous function
        testcases-=1
        
if __name__=='__main__':
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
    
power = lambda a,b:a**b##write the lambda expression in one line here
