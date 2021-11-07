from collections import Counter  #최빈값 구하기 위함

num1 = int(input())  
num = []
for i in range(num1) :
    num2 = int(input())
    num.append(num2)

k=Counter(num).most_common()

if num1 == 1 :
    exp = num1 
    med = num1
    mod = num1
    ran = 0
    print(exp, med, mod, ran)

else : 
    exp = round(sum(num) / num1) 
    med = num[num1//2]
    if k[0][1] == k[1][1] :
        mod = k[1][0]
    else :
        mod = k[0][0]
    
    print("exp :",exp)  
    print("med :",med)
    print("mod :",mod)
    ran = max(num) - min(num)
    print("ran :",ran)




