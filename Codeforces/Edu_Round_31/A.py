n,t=map(int,input().split())
ls=list(map(int,input().split()))
i=0
sum1=0
while(i<n):
	sum1+=(86400-ls[i])
	if(sum1>=t):
		print(i+1)
		exit()
	i+=1