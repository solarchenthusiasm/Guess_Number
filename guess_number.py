
import random

start = input('pleae key in the bordline condition_Min :')
start = int(start)
end = input('pleae key in the bordline condition_Max :')
end = int(end)
r = random.randint(start,end)
count = 0
while True:
	count += 1 # count = count + 1
	num = input('Please guess the number :')
	num = int(num)
	if num == r:
		print('Congrat !!!')
		print('Guess', count, 'times')
		break
	elif num > r and r > start:
		print('Higer than amswer')
	elif num < r :
		print('Lower than answer')
	print('Guess', count, 'times')






