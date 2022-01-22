input_str = input()
sum = 0
left = 0
for i in range(len(input_str)):
    if input_str[i] == '(':
        left=left+1
    elif input_str[i] == ')':
        left=left-1
        if input_str[i-1] == '(':
            sum=sum+left
        else:
            sum=sum+1
print(sum)