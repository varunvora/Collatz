from data import *
count = 0
big = list(d.keys())[-1]
print("We are starting from ", big+1)

for i in range(big+1, (big+1)+100000):
	d, count
	d[i-1] = count		
	count = 0
	n = i
	while(n != 1):
		if n < i:
			d[i] = count + d[n]
		if n%2==0:
			n/=2
			count+=1
		else:
			n = (3*n + 1)/2
			count+=2

op = open('data.py', 'w')
new_str = 'd = ' + str(d)
op.write(new_str)
op.close()

print("We went upto", big+100000)
most = max(d.values())
for num, steps in d.items():
    if steps == most:
        print("Maximum is for ", num, " : ", steps, " steps")
