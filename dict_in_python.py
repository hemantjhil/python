{
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver code
def main():
    
    # testcase input
    testcase = int(input())
    
    # looping through testcases
    while(testcase > 0):
        
        n = int(input())
        sum = int(input())
        dict = {}
        x = n
        p = [int(i) for i in (input().split())]
        
        for i in p:
            dict[i] = 0
                
        for i in p:
            dict[i] +=1
    
        if pair_sum(dict, n, p, sum) is True:
            print ("Yes")
        else:
            print ("No")
        
        testcase -= 1
if __name__ == '__main__':
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
# Function to check if pair 
# with given sum exists
def pair_sum(dict, n, arr, sum):
    
    # Your code here
    # Hint: You can use 'in' to find if any key is in dict
    for i in dict.keys():
        dict2=dict.copy()
        dict2.pop(i)
        if((sum-i)in dict2.keys()):
            return True
            break
    
    return False
