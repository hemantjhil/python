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
        
        i = 0
        dict = {}
        while i < n:
            flag = False
            delete = False
            query = input().split()
            if(query[0] == 'i'):
                insert_dict(query, dict)
                print ("Inserted")
            
            if(query[0] == 'd'):
                if del_dict(query, dict) is False:
                    print ("-1")
                else:
                    print ("Deleted")
            
            if(query[0] == 'p'):
                if(print_dict(query[1], dict) is False):
                    print ("-1")
                    
            i+=1
            
        testcase -= 1
if __name__ == '__main__':
    main()
}
''' This is a function problem.You only need to complete the function given below '''
#User function Template for python3
# insert into dictionary
def insert_dict(query, dict):
    
    # Your code here
    #q=query.split(" ")
    dict[query[1]]=query[2]
    
# deleting from dictionary
def del_dict(query, dict):
    if(query[1] in dict):
        #print("Deleted")
        del dict[query[1]]
        return True
    return False
    # Your code here
    
    
    
    
# print marks of required name
def print_dict(key, dict):
    if(key in dict):
        print("Marks of "+ key+ " is " +dict[key])
        return True
    return False
    # Your code here
    
