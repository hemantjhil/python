{
#Initial Template for Python 3
//Position this line where user code will be pasted.
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        # size of array
        size_array = int(input())
        
        # array elements input
        array = input().split()
        # print (array)
        arr = list()
        for i in array:
            arr.append(int(i))
            
        # print (arr)
        
        # calling function to check zero
        if(check_zero(size_array, arr) is True):
            print ("Yes")
        else:
            print ("No")
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
# Function to check zero at 
# start and end index
def check_zero(size_array, arr):
    
    # complete the if statement to check
    # if first or last element in list is 0
    if( arr[0]==0 or arr[size_array-1]==0):
        return True
    return False
