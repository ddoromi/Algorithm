import sys
sys.stdin = open('1240.txt')

T = int(input())
for test_case in range(1, T + 1):
	N, M = map(int, input().split())
	data = []
	password = []
	counts = [1]
	numbers = []
	Sum = 0
	
	for n in range(N):
		data.append(list((input())))

	for i in range(N):
		for j in range(1, M + 1):
			if data[i][-j] == '1':
				password = data[i][-j-55: -j+1]
				break
	
	for i in range(1, 56):
		if i % 7 != 0:
			if password[i - 1] != password[i]:
				counts.append(1)
			else:
				counts[-1] += 1
		if i % 7 == 0 or i == 55:
			if counts == [3, 2, 1, 1]:
				numbers.append(0)
			elif counts == [2, 2, 2, 1]:
				numbers.append(1)
			elif counts == [2, 1, 2, 2]:
				numbers.append(2)
			elif counts == [1, 4, 1, 1]:
				numbers.append(3)
			elif counts == [1, 1, 3, 2]:
				numbers.append(4)
			elif counts == [1, 2, 3, 1]:
				numbers.append(5)
			elif counts == [1, 1, 1, 4]:
				numbers.append(6)
			elif counts == [1, 3, 1, 2]:
				numbers.append(7)
			elif counts == [1, 2, 1, 3]:
				numbers.append(8)
			else:
				numbers.append(9)
			counts = [1]
	
	for i in range(7):
		if i % 2 != 0:
			Sum += numbers[i]
		else:
			Sum += numbers[i] * 3

	if (Sum + numbers[-1]) % 10 == 0:
		print('#{} {}'.format(test_case, sum(numbers)))
	else:
		print('#{} {}'.format(test_case, 0))
