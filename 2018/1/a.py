import sys

try:
	with open(sys.argv[1], 'r') as f:
		nums = f.read()
except:
	sys.exit('Could not read file')

nums = nums.strip()
nums = [int(i) for i in nums.split('\n')]

print(sum(nums))