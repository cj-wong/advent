import sys

try:
	with open(sys.argv[1], 'r') as f:
		ids = f.read()
except:
	sys.exit('Could not read file')

ids = ids.strip().split()

nuid = []

for _id in ids:
	_id = list(_id)
	uid = list(set(_id))
	nuid.append(list(set([_id.count(_uid) for _uid in uid])))

twos = threes = 0

for _nuid in nuid:
	if 2 in _nuid:
		twos += 1
	if 3 in _nuid:
		threes += 1

print(twos*threes)