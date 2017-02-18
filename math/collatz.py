def even(num):
	return num /2

def odd(num):
	return num * 3 + 1 

def seprator(char, rep):
	for i in range(rep):
		print(char, end='')
                print(char)




num = int(input())
steps = 0




while num != 1:
	steps = steps + 1
	if (num % 2) == 0:
		num = even(num)
	else:
		num = odd(num)
	print("Step #{}, number is: {}".format(steps, num))


seprator('-',5)
print("It took {} steps to get to one".format(steps))
