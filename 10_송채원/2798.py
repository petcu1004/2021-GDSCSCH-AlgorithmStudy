N,M=map(int,input().split()) 

card=input().split() 
for i in range(N): 
    card[i]=int(card[i]) 
sum=[] 

for i in range(N): 
    for j in range((i+1),N): 
        for k in range(j+1,N): 
            if card[i]+card[j]+card[k]>M:continue
            else: sum.append(card[i]+card[j]+card[k]) 
            
print(max(sum))