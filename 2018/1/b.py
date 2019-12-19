import sys

try:
	with open(sys.argv[1], 'r') as f:
		nums = f.read()
except:
	sys.exit('Could not read file')

nums = nums.strip()
nums = [int(i) for i in nums.split('\n')]

_sum = 0
sums = []

while True:
	for n in nums:
		_sum += n
		if _sum in sums:
			print(_sum)
			sys.exit(0)
		else:
			sums.append(_sum)

print(sums)