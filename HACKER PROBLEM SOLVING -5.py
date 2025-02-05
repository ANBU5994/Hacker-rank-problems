'''Consider a list (list = []). You can perform the following commands:

insert i e: Insert integer  at position .
print: Print the list.
remove e: Delete the first occurrence of integer .
append e: Insert integer  at the end of the list.
sort: Sort the list.
pop: Pop the last element from the list.
reverse: Reverse the list.
Initialize your list and read in the value of  followed by  lines of commands where each command will be of
the  types listed above. Iterate through each command in order and perform the corresponding operation on your list.'''

if __name__ == '__main__':
    N = int(input())
    x=[]
    cmd=[input().strip() for _ in range(N)]
    for i in range(N):
        temp=list(cmd[i].split(' '))
        if temp[0]=='insert':
            x.insert(int(temp[1]),int(temp[2]))
        elif temp[0]=='print':
             print(x)
        elif temp[0]=='remove':
            x.remove(int(temp[1]))
        elif temp[0]=='append':
            x.append(int(temp[1]))
        elif temp[0]=='sort':
            x.sort()
        elif temp[0]=='pop':
            x.pop(-1)
        elif temp[0]=='reverse':
            x.reverse()
            