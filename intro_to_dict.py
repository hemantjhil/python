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
        
        dict = create_dict(arr)
        
        for key in sorted(dict.keys()):
            print (key, dict[key])
        
        testcases -= 1
 
if __name__ == '__main__':
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
# Function to create dictionary
def create_dict(arr):
    
    dict = {}
    
    # Your code here
    # Hint: use loop to iterate through arr
    # and assign key value to the dict
    for i in range(0,len(arr)):
        dict[arr[i][0]]=arr[i][1]
    
    
    
    return dict
