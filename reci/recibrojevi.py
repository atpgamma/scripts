import sys

brojevi = ['jedan','dva','tri','cetiri','pet','sest','sedam','osam','devet','deset','nula','sto']


if(len(sys.argv) > 1):
	rec = sys.argv[1]
	f = open('reci.txt','r')
	out = open('out.txt','w')
	for line in f.readlines():
		if rec in line:
			print(line)
else:
	f = open('reci.txt','r')
	out = open('out.txt','w')
	for line in f.readlines():
		for broj in brojevi:
			if broj in line:
				print(line)
				out.write(line)

	f.close()
	out.close()
