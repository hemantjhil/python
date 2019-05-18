def count_substring(string, sub_string):
    k=0
    for i in range(0,len(string)-len(sub_string)+1):
        if(sub_string in string[i:i+len(sub_string)]):
            k=k+1
    return k

if __name__ == '__main__':
    string = input().strip()
    sub_string = input().strip()
    
    count = count_substring(string, sub_string)
    print(count)