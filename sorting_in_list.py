{
#Initial Template for Python 3
//Position this line where user code will be pasted.
    
# Driver Code
def main():
    
    # Testcase input
    testcases = int(input())
    
    # Looping through testcases
    while(testcases > 0):
        size_arr = int(input())
        
        name = input().split()
        marks = input().split()
        arr = list()
        for i in range(0, size_arr, 1):
            arr.append((name[i], marks[i]))
        
        arr.sort(key = customSort)
        
        for i in arr:
            print (i[0], i[1], end = " ")
        
        print ()
        testcases -= 1
 
if __name__ == '__main__':
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
# Function to sort using comparator
def customSort(arr):
    
    # Your code here
    # Hint : Should be a return statement
    getkey=arr[-1]
    return sorted(arr,key=lambda x:x[-1])
