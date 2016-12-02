brojevi = ['jedan','dva','tri','cetiri','pet','sest','sedam','osam','devet','deset']


f = open('reci.txt','r')
for line in f.readlines():
	for broj in brojevi:
		if broj in line:
			print(line)

f.close()
