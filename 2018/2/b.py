import sys

try:
	with open(sys.argv[1], 'r') as f:
		ids = f.read()
except:
	sys.exit('Could not read file')

ids = ids.strip().split()

answer = ''

for _id in ids:
	others = ids[:]
	others.remove(_id)
	for other in others:
		diffs = 0
		for _a, _b in zip(_id, other):
			if _a != _b and diffs == 0:
				diffs += 1
			elif _a != _b:
				diffs += 1
				break
		if diffs == 1:
			for _a, _b in zip(_id, other):
				if _a == _b:
					answer += _a
			print(answer)
			sys.exit(0)