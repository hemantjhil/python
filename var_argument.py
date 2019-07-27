{
#Initial Template for Python 3
//Position this line where user code will be pasted.
def main():
    testcases=int(input()) #testcases
    while(testcases>0):
        single=int(input())
        multivar(single,4,5,6,7) ## The single argument and multiarguments are passed to multivar function
        testcases-=1
        
if __name__=='__main__':
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
def multivar(a, *var): 
    ##*var takes multiple arguments inside it
    ## print the sum of a + elements of var
    print (a+sum(var))
